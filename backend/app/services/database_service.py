"""Service helpers for fetching repository metadata from the database."""

from __future__ import annotations

from datetime import datetime, timezone

from app.schemas.database_schema import FileDescriptor, RepositorySnapshot


def fetch_repository_snapshot(repo_id: int) -> RepositorySnapshot:
  """Retrieve a repository snapshot for the provided `repo_id`.

  This stub returns deterministic placeholder data to unblock the frontend while
  the real database layer is implemented.
  """

  return RepositorySnapshot(
    repository_name=f"Repository {repo_id}",
    files=[
      FileDescriptor(path="README.md", type="file"),
      FileDescriptor(path="src", type="directory"),
      FileDescriptor(path="src/main.py", type="file"),
    ],
  )


def last_refreshed_at() -> str:
  """Utility helper that returns the current refresh timestamp."""

  return datetime.now(tz=timezone.utc).isoformat()


__all__ = ["fetch_repository_snapshot", "last_refreshed_at"]

