"""Schema definitions for agent WebSocket events."""

from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel


class UserTextMessage(BaseModel):
  type: Literal["USER_TEXT_MESSAGE"]
  payload: str


class ToolCallSuccess(BaseModel):
  type: Literal["TOOL_CALL_SUCCESS"]
  call_id: str


ClientEvent = Union[UserTextMessage, ToolCallSuccess]


class RunStarted(BaseModel):
  type: Literal["RUN_STARTED"]


class TextMessageContent(BaseModel):
  type: Literal["TEXT_MESSAGE_CONTENT"]
  payload: str


class ToolCallStart(BaseModel):
  type: Literal["TOOL_CALL_START"]
  call_id: str
  payload: dict


class RunFinished(BaseModel):
  type: Literal["RUN_FINISHED"]


ServerEvent = Union[RunStarted, TextMessageContent, ToolCallStart, RunFinished]


__all__ = [
  "ClientEvent",
  "RunFinished",
  "RunStarted",
  "ServerEvent",
  "TextMessageContent",
  "ToolCallStart",
  "ToolCallSuccess",
  "UserTextMessage",
]

