# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    display_name: Optional[str]

    display_name_contains: Optional[str]

    expand: Optional[SequenceNotStr[str]]
    """Fields to expand on each directory file."""

    file_id: Optional[str]

    include_deleted: bool

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]

    unique_id: Optional[str]

    updated_at_on_or_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items updated at or after this timestamp (inclusive)"""

    updated_at_on_or_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items updated at or before this timestamp (inclusive)"""
