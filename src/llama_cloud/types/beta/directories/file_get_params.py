# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FileGetParams"]


class FileGetParams(TypedDict, total=False):
    directory_id: Required[str]

    expand: Optional[SequenceNotStr[str]]
    """Fields to expand."""

    organization_id: Optional[str]

    project_id: Optional[str]
