# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["JobDataPointListParams"]


class JobDataPointListParams(TypedDict, total=False):
    job_type: Required[Literal["classify", "extract", "parse"]]
    """Job type to query."""

    created_at_on_or_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items created at or after this timestamp (inclusive)"""

    created_at_on_or_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items created at or before this timestamp (inclusive)"""

    hours: int
    """Hours of history to include."""

    organization_id: Optional[str]

    page_size: Optional[int]
    """Number of items per page."""

    page_token: Optional[str]
    """Cursor token for the next page."""

    project_id: Optional[str]

    status: Optional[SequenceNotStr[str]]
    """Filter by status."""
