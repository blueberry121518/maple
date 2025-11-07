"""Background job orchestration for repository onboarding."""

from __future__ import annotations

import re
from datetime import datetime, timezone


class OnboardingJobError(ValueError):
  """Raised when an onboarding request payload is invalid."""


GITHUB_REPO_PATTERN = re.compile(r"^https://github\.com/[\w.-]+/[\w.-]+/?$")


def trigger_onboarding_job(url: str) -> None:
  """Validate the GitHub URL and enqueue a background onboarding job.

  This placeholder implementation simply logs the accepted request. In a real
  system, this would push a message onto a queue or task runner and return
  immediately.
  """

  if not GITHUB_REPO_PATTERN.match(url):
    raise OnboardingJobError(f"Invalid GitHub repository URL: {url}")

  # Simulate asynchronous job dispatch.
  print(f"[{datetime.now(tz=timezone.utc).isoformat()}] Onboarding queued for {url}")


__all__ = ["OnboardingJobError", "trigger_onboarding_job"]

