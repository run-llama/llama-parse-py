# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReviewChangeFieldsParams", "Change"]


class ReviewChangeFieldsParams(TypedDict, total=False):
    changes: Required[Iterable[Change]]
    """Changes to apply, in order."""

    revision: Required[int]
    """The review's revision as the caller last read it."""

    organization_id: Optional[str]

    project_id: Optional[str]


class Change(TypedDict, total=False):
    """One change to one field."""

    change: Required[Literal["clear", "confirm", "correct", "restore", "undo"]]
    """confirm, correct to `value`, clear, restore the model's value, or undo."""

    path: Required[str]
    """JSON Pointer of the field."""

    value: object
    """The corrected value, for `correct`."""
