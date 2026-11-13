# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReviewReopenParams"]


class ReviewReopenParams(TypedDict, total=False):
    revision: Required[int]
    """The review's revision as the caller last read it."""

    organization_id: Optional[str]

    project_id: Optional[str]
