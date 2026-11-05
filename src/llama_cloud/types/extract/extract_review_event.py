# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ExtractReviewEvent",
    "Detail",
    "DetailExtractReviewCreatedDetail",
    "DetailExtractReviewRejectedDetail",
    "DetailExtractReviewSignedOffDetail",
]


class DetailExtractReviewCreatedDetail(BaseModel):
    """What a `created` entry records: where review was turned on, and its settings."""

    confidence_threshold: float
    """Fields read below this confidence are flagged."""

    fields_in_scope: List[str]
    """JSON Pointers of the fields the threshold applies to; empty means all."""

    origin: Literal["api", "edit", "history", "run"]
    """Turned on as the job ran, from History, by a first edit, or by the API."""

    required_fields: List[str]
    """JSON Pointers of fields flagged when empty."""


class DetailExtractReviewRejectedDetail(BaseModel):
    """What a `rejected` entry records."""

    reason: str
    """Why the result was rejected."""


class DetailExtractReviewSignedOffDetail(BaseModel):
    """What a `flags_signed_off` entry records."""

    paths: List[str]
    """JSON Pointers of the flagged fields confirmed as part of approving."""


Detail: TypeAlias = Union[
    DetailExtractReviewCreatedDetail, DetailExtractReviewRejectedDetail, DetailExtractReviewSignedOffDetail, None
]


class ExtractReviewEvent(BaseModel):
    """One entry in a review's history."""

    id: str
    """Unique identifier of the entry."""

    actor_id: str
    """ID of the user who acted."""

    created_at: datetime
    """When it happened."""

    kind: Literal[
        "approved",
        "created",
        "field_cleared",
        "field_confirmed",
        "field_corrected",
        "field_restored",
        "field_undone",
        "flags_signed_off",
        "rejected",
        "reopened",
    ]
    """What happened."""

    detail: Optional[Detail] = None
    """
    The settings for `created`, the reason for `rejected`, and the fields for
    `flags_signed_off`; null for the rest.
    """

    path: Optional[str] = None
    """JSON Pointer of the field it changed."""

    value_after: Optional[object] = None
    """The field's value after the change."""

    value_before: Optional[object] = None
    """The field's value before the change."""
