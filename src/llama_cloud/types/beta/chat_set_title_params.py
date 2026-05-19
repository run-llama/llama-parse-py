# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatSetTitleParams"]


class ChatSetTitleParams(TypedDict, total=False):
    first_message: Required[str]
    """First user message of the session, used to infer a short title."""

    organization_id: Optional[str]

    project_id: Optional[str]
