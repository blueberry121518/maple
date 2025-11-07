"""Application configuration and settings management."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv


load_dotenv()


def _as_bool(value: str | None, default: bool = False) -> bool:
  if value is None:
    return default
  return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(slots=True)
class Settings:
  """Typed configuration pulled from environment variables."""

  app_name: str = os.getenv("APP_NAME", "Maple API")
  database_url: str = os.getenv("DATABASE_URL", "sqlite:///./maple.db")
  dev_mode: bool = _as_bool(os.getenv("DEV_MODE"), default=True)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
  return Settings()


settings = get_settings()

__all__ = ["Settings", "get_settings", "settings"]

