# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentGetChunksParams"]


class DocumentGetChunksParams(TypedDict, total=False):
    pipeline_id: Required[str]

    project_id: Optional[str]
