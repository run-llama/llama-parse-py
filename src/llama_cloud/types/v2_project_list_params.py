# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["V2ProjectListParams"]


class V2ProjectListParams(TypedDict, total=False):
    name: Optional[str]

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]
