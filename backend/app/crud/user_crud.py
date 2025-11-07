"""User-specific CRUD helpers."""

from typing import Sequence

from app.crud.base_crud import CRUDBase
from app.models.user_model import User


class UserCRUD(CRUDBase[User]):
  """Placeholder implementation until the database layer is wired up."""

  def get_multi(self) -> Sequence[User]:  # pragma: no cover - placeholder
    return []

  def create(self, obj_in: User) -> User:  # pragma: no cover - placeholder
    return obj_in


user_crud = UserCRUD()

__all__ = ["user_crud", "UserCRUD"]

