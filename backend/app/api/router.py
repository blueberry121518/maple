"""Aggregate FastAPI router that mounts all controllers."""

from fastapi import APIRouter

from app.controllers.agent_controller import router as agent_router
from app.controllers.database_controller import router as database_router
from app.controllers.onboarding_controller import router as onboarding_router


api_router = APIRouter(prefix="/api")

api_router.include_router(onboarding_router, prefix="/onboard", tags=["onboarding"])
api_router.include_router(database_router, prefix="/fetch", tags=["database"])
api_router.include_router(agent_router, prefix="/agent", tags=["agent"])

