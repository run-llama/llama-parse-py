# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DocumentGetStatusCountsParams"]


class DocumentGetStatusCountsParams(TypedDict, total=False):
    data_source_id: Optional[str]

    file_id: Optional[str]

    only_direct_upload: bool
