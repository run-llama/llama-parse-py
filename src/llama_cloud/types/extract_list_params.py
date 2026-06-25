# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ExtractListParams"]


class ExtractListParams(TypedDict, total=False):
    configuration_id: Optional[str]
    """Filter by configuration ID"""

    created_at_on_or_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items created at or after this timestamp (inclusive)"""

    created_at_on_or_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items created at or before this timestamp (inclusive)"""

    document_input_type: Optional[str]
    """Filter by document input type (file_id or parse_job_id)"""

    document_input_value: Optional[str]
    """Deprecated: use file_input instead"""

    expand: SequenceNotStr[str]
    """Additional fields to include: configuration, extract_metadata"""

    file_input: Optional[str]
    """Filter by file input value"""

    job_ids: Optional[SequenceNotStr[str]]
    """Filter by specific job IDs"""

    organization_id: Optional[str]

    page_size: Optional[int]
    """Number of items per page"""

    page_token: Optional[str]
    """Token for pagination"""

    project_id: Optional[str]

    status: Optional[Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "THROTTLED"]]
    """Filter by status"""
