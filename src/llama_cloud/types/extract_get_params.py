# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ExtractGetParams"]


class ExtractGetParams(TypedDict, total=False):
    expand: SequenceNotStr[str]
    """Additional fields to include: configuration, extract_metadata"""

    organization_id: Optional[str]

    project_id: Optional[str]
