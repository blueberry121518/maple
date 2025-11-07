"""HTTP endpoints for fetching repository metadata."""

from fastapi import APIRouter, Query

from app.schemas.database_schema import RepositorySnapshot
from app.services.database_service import fetch_repository_snapshot


router = APIRouter()


@router.get(
  "/files",
  response_model=RepositorySnapshot,
  summary="Fetch repository file tree",
)
async def fetch_repository_files(repo_id: int = Query(..., description="Repository identifier")) -> RepositorySnapshot:
  """Return the file tree snapshot for the requested repository."""

  return fetch_repository_snapshot(repo_id)

