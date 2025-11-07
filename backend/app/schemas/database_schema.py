"""Pydantic models for representing repository metadata responses."""

from typing import Literal

from pydantic import BaseModel


class FileDescriptor(BaseModel):
  path: str
  type: Literal["file", "directory"]


class RepositorySnapshot(BaseModel):
  repository_name: str
  files: list[FileDescriptor]

