# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    created_at_on_or_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    created_at_on_or_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]

    source_directory_id: Optional[str]

    status: Optional[Literal["PENDING", "THROTTLED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]]
