# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExtractReview", "FieldActions", "Flag", "FlagCell"]


class FieldActions(BaseModel):
    """The latest thing a person did to one field."""

    action: Literal["clear", "confirm", "correct"]
    """confirm, correct or clear."""

    actor_id: str
    """ID of the user who acted."""

    at: datetime
    """When they acted."""

    value: Optional[object] = None
    """The corrected value, for `correct`."""


class FlagCell(BaseModel):
    """Where in a list the least confident value is."""

    row: int
    """Index of the row, from 0."""

    column: Optional[str] = None
    """Property of the row, when rows are objects."""


class Flag(BaseModel):
    """A field the review asks a person to check."""

    handled: bool
    """Whether someone confirmed, corrected or cleared it."""

    path: str
    """JSON Pointer of the field."""

    reason: Literal["below_threshold", "required_empty"]
    """below_threshold, or required_empty for a required field left empty."""

    cell: Optional[FlagCell] = None
    """Where in a list the least confident value is."""

    confidence: Optional[float] = None
    """The field's confidence; for a list, its least confident value."""


class ExtractReview(BaseModel):
    """
    An extract job's review: its settings, flags, field actions and decision,
    with the result as read and as reviewed.
    """

    id: str
    """Unique identifier of the review."""

    confidence_threshold: float
    """Fields read below this confidence are flagged."""

    created_at: datetime
    """When review was turned on."""

    decided_at: Optional[datetime] = None
    """When it was approved or rejected."""

    decided_by: Optional[str] = None
    """ID of the user who approved or rejected it."""

    decided_reason: Optional[str] = None
    """Why it was rejected."""

    field_actions: Dict[str, FieldActions]
    """The latest action per field, keyed by JSON Pointer."""

    fields_in_scope: List[str]
    """JSON Pointers of the fields the threshold applies to; empty means all."""

    flags: List[Flag]
    """Fields the review asks a person to check."""

    job_id: str
    """The extract job reviewed."""

    open_flags: List[str]
    """JSON Pointers of flagged fields nobody checked."""

    original_result: Optional[Dict[str, object]] = None
    """The result as the model read it."""

    required_fields: List[str]
    """JSON Pointers of fields flagged when empty."""

    retain_until: datetime
    """When the job and its document may be deleted."""

    reviewed_result: Dict[str, object]
    """The result with the field actions."""

    revision: int
    """Bumped by every change; actions name the one they saw."""

    source_file_id: Optional[str] = None
    """
    The file the job read, or the file behind the parse job it read; null for a URL.
    """

    status: Literal["approved", "pending", "rejected"]
    """pending until approved or rejected."""

    updated_at: datetime
    """When the review last changed."""
