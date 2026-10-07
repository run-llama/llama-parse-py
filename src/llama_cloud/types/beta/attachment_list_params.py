# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AttachmentListParams"]


class AttachmentListParams(TypedDict, total=False):
    source_id: Required[str]
    """File UUID or directory file ID (dfl-...)."""

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]
