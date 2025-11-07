"""Base CRUD operations to share across resources."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Generic, TypeVar


ModelT = TypeVar("ModelT")


class CRUDBase(Generic[ModelT]):
  """A minimal CRUD interface intended to wrap SQLAlchemy operations."""

  def get_multi(self) -> Sequence[ModelT]:  # pragma: no cover - placeholder
    raise NotImplementedError

  def create(self, obj_in: ModelT) -> ModelT:  # pragma: no cover - placeholder
    raise NotImplementedError

