# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ExtractionAgentListParams"]


class ExtractionAgentListParams(TypedDict, total=False):
    include_default: bool
    """Whether to include default agents in the results"""

    organization_id: Optional[str]

    page_size: int
    """Number of items per page"""

    page_token: Optional[str]
    """Cursor from the previous page's `next_page_token`."""

    project_id: Optional[str]
