"""WebSocket endpoint for agent interaction events."""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.services.agent_gateway import agent_gateway


router = APIRouter()


@router.websocket("/interaction")
async def agent_interaction(websocket: WebSocket) -> None:
  """Establish a persistent WebSocket channel for agent communication."""

  await agent_gateway.connect(websocket)
  try:
    while True:
      event = await websocket.receive_json()
      await agent_gateway.handle_event(event)
  except WebSocketDisconnect:
    agent_gateway.disconnect(websocket)

