# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatchCancelParams"]


class BatchCancelParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    reason: Optional[str]
    """Optional reason for cancelling the job"""

    temporal_namespace: Annotated[str, PropertyInfo(alias="temporal-namespace")]
