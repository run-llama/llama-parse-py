# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ReviewListEventsParams"]


class ReviewListEventsParams(TypedDict, total=False):
    organization_id: Optional[str]

    page_size: int
    """Events per page."""

    page_token: Optional[str]
    """Token from the previous page."""

    project_id: Optional[str]
