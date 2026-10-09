# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["IndexListParams"]


class IndexListParams(TypedDict, total=False):
    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]

    source_directory_id: Optional[str]
