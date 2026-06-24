# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["JobItemListParams"]


class JobItemListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return"""

    offset: int
    """Number of items to skip"""

    organization_id: Optional[str]

    project_id: Optional[str]

    status: Optional[Literal["cancelled", "completed", "failed", "pending", "processing", "skipped"]]
    """Filter items by status"""
