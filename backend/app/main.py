from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
  if settings.dev_mode:
    print("Starting Maple API in development mode...")
  yield
  if settings.dev_mode:
    print("Shutting down Maple API...")


app = FastAPI(
  title="Maple API",
  version="0.1.0",
  lifespan=lifespan,
)

app.include_router(api_router)

