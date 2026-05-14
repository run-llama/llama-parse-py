# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DirectoryListParams"]


class DirectoryListParams(TypedDict, total=False):
    include_deleted: bool

    name: Optional[str]

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]

    type: Optional[Literal["user", "index"]]
