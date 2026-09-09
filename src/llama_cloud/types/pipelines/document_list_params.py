# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    file_id: Optional[str]

    limit: int

    only_api_data_source_documents: Optional[bool]

    only_direct_upload: Optional[bool]

    skip: int

    status_refresh_policy: Literal["cached", "ttl"]
