# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SplitDocumentInputParam"]


class SplitDocumentInputParam(TypedDict, total=False):
    """Document input specification for beta API."""

    type: Required[str]
    """The beta `POST /api/v1/beta/split/jobs` endpoint accepts only `file_id`.

    To use a Parse job as input, call `POST /api/v1/split/jobs` instead, where you
    can pass the Parse job ID as `file_input`.
    """

    value: Required[str]
    """Document identifier."""
