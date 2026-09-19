# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RetrieverListPaginatedParams"]


class RetrieverListPaginatedParams(TypedDict, total=False):
    include_total: bool
    """Return `total_size`, a count of every row matching the filter.

    It is a second query on every page, so it is off unless asked for.
    """

    name: Optional[str]

    organization_id: Optional[str]

    page_size: int
    """Number of items per page"""

    page_token: Optional[str]
    """Cursor from the previous page's `next_page_token`."""

    project_id: Optional[str]
