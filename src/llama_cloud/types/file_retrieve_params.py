# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["FileRetrieveParams"]


class FileRetrieveParams(TypedDict, total=False):
    expand: Optional[SequenceNotStr[str]]
    """Fields to expand."""

    organization_id: Optional[str]

    project_id: Optional[str]
