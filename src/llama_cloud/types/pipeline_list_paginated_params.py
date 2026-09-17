# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["PipelineListPaginatedParams"]


class PipelineListPaginatedParams(TypedDict, total=False):
    name: Optional[str]

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    pipeline_type: Optional[Literal["MANAGED", "PLAYGROUND"]]

    project_id: Optional[str]
