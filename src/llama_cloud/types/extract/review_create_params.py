# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ReviewCreateParams"]


class ReviewCreateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    confidence_threshold: float
    """Fields read below this confidence are flagged."""

    fields_in_scope: SequenceNotStr[str]
    """JSON Pointers of the fields the threshold applies to; empty means all."""

    required_fields: Optional[SequenceNotStr[str]]
    """JSON Pointers of fields flagged when empty; defaults to the schema's required."""
