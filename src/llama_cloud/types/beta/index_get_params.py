# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["IndexGetParams"]


class IndexGetParams(TypedDict, total=False):
    expand: List[Literal["sync_in_progress"]]
    """Fields to expand. Supported value: sync_in_progress."""

    organization_id: Optional[str]

    project_id: Optional[str]
