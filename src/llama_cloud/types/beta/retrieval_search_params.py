# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RetrievalSearchParams"]


class RetrievalSearchParams(TypedDict, total=False):
    index_id: Required[str]
    """ID of the index to search within."""

    organization_id: Optional[str]

    project_id: Optional[str]

    file_name: Optional[str]
    """Exact file name to match."""

    file_name_contains: Optional[str]
    """Substring match on file name (case-insensitive)."""

    limit: Optional[int]
    """Maximum number of files to return."""
