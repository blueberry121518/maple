"""WebSocket gateway for orchestrating agent message flow."""

from __future__ import annotations

import asyncio
from typing import Any

from fastapi import WebSocket
from pydantic import TypeAdapter, ValidationError

from app.schemas.agent_schema import (
  ClientEvent,
  RunFinished,
  RunStarted,
  ServerEvent,
  TextMessageContent,
  ToolCallStart,
  ToolCallSuccess,
  UserTextMessage,
)

CLIENT_EVENT_ADAPTER = TypeAdapter(ClientEvent)


class AgentGateway:
  """Stateful gateway that validates and routes agent WebSocket events."""

  def __init__(self) -> None:
    self._connections: set[WebSocket] = set()

  async def connect(self, websocket: WebSocket) -> None:
    await websocket.accept()
    self._connections.add(websocket)
    await self._send_event(websocket, RunStarted(type="RUN_STARTED"))

  def disconnect(self, websocket: WebSocket) -> None:
    self._connections.discard(websocket)

  async def handle_event(self, raw_event: Any) -> None:
    """Validate inbound events and dispatch the corresponding response."""

    try:
      event = self._parse_client_event(raw_event)
    except ValidationError as exc:
      await self._broadcast(
        TextMessageContent(type="TEXT_MESSAGE_CONTENT", payload=f"Invalid event received: {exc}")
      )
      return

    if isinstance(event, UserTextMessage):
      await self._handle_user_text(event)
    elif isinstance(event, ToolCallSuccess):
      await self._handle_tool_call_success(event)

  async def _handle_user_text(self, event: UserTextMessage) -> None:
    """Placeholder behaviour for user-submitted chat messages."""

    await self._broadcast(
      TextMessageContent(type="TEXT_MESSAGE_CONTENT", payload=f"Agent received: {event.payload}")
    )
    await asyncio.sleep(0)
    await self._broadcast(
      ToolCallStart(
        type="TOOL_CALL_START",
        call_id="ui_cmd_preview",
        payload={
          "name": "navigateTo",
          "args": {"resource": event.payload},
        },
      )
    )

  async def _handle_tool_call_success(self, event: ToolCallSuccess) -> None:
    await self._broadcast(
      TextMessageContent(
        type="TEXT_MESSAGE_CONTENT",
        payload=f"Acknowledged completion of {event.call_id}",
      )
    )
    await self._broadcast(RunFinished(type="RUN_FINISHED"))

  async def _send_event(self, websocket: WebSocket, event: ServerEvent) -> None:
    await websocket.send_json(event.model_dump())

  async def _broadcast(self, event: ServerEvent) -> None:
    for connection in list(self._connections):
      await self._send_event(connection, event)

  @staticmethod
  def _parse_client_event(payload: Any) -> ClientEvent:
    """Leverage discriminated unions to validate inbound WebSocket events."""

    return CLIENT_EVENT_ADAPTER.validate_python(payload)


agent_gateway = AgentGateway()

__all__ = ["AgentGateway", "agent_gateway"]

