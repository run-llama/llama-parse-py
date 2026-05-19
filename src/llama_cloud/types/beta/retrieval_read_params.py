# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RetrievalReadParams"]


class RetrievalReadParams(TypedDict, total=False):
    file_id: Required[str]
    """ID of the file to read."""

    index_id: Required[str]
    """ID of the index the file belongs to."""

    organization_id: Optional[str]

    project_id: Optional[str]

    max_length: Optional[int]
    """Maximum number of characters to read from the offset."""

    offset: int
    """Starting character offset."""
