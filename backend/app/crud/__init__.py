"""CRUD utilities for interacting with the persistence layer."""

from app.crud.base_crud import CRUDBase
from app.crud.user_crud import user_crud

__all__ = ["CRUDBase", "user_crud"]

