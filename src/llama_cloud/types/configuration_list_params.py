# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ConfigurationListParams"]


class ConfigurationListParams(TypedDict, total=False):
    latest_only: bool
    """Return only the latest version per configuration name."""

    name: Optional[str]
    """Filter by configuration name."""

    organization_id: Optional[str]

    page_size: Optional[int]
    """Number of items per page."""

    page_token: Optional[str]
    """Pagination token."""

    product_type: Optional[
        List[Literal["classify_v2", "extract_v2", "parse_v2", "split_v1", "spreadsheet_v1", "unknown"]]
    ]
    """Filter by one or more product types. Repeat the parameter for multiple values."""

    project_id: Optional[str]
