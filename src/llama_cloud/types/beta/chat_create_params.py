# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ChatCreateParams"]


class ChatCreateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    index_ids: Optional[SequenceNotStr[str]]
    """Indexes this session will retrieve from.

    Once set and the first message has been sent, the source set is locked for the
    session's lifetime. Leave null to create an unbound session.
    """
