"""HTTP endpoints for repository onboarding requests."""

from fastapi import APIRouter, HTTPException, Response, status

from app.services.onboarding_service import OnboardingJobError, trigger_onboarding_job


router = APIRouter()


@router.get("", status_code=status.HTTP_202_ACCEPTED, summary="Start GitHub repository onboarding")
async def onboard_repository(url: str) -> Response:
  """Kick off asynchronous indexing for a GitHub repository.

  The request immediately returns 202 to signal the job was accepted.
  """

  try:
    trigger_onboarding_job(url)
  except OnboardingJobError as exc:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc
  return Response(status_code=status.HTTP_202_ACCEPTED)

