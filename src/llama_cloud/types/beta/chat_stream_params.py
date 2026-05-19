# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ChatStreamParams"]


class ChatStreamParams(TypedDict, total=False):
    index_ids: Required[SequenceNotStr[str]]
    """Indexes to retrieve data from."""

    prompt: Required[str]
    """User message for this chat turn."""

    organization_id: Optional[str]

    project_id: Optional[str]
