# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["RetrievalSearchResponse", "File"]


class File(BaseModel):
    """A file returned by search."""

    file_id: str
    """ID of the file."""

    file_name: str
    """Display name of the file."""


class RetrievalSearchResponse(BaseModel):
    """File search results."""

    files: List[File]
    """Matching files with names."""
