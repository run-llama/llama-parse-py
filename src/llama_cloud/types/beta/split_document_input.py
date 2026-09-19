# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SplitDocumentInput"]


class SplitDocumentInput(BaseModel):
    """Document input specification for beta API."""

    type: str
    """The beta `POST /api/v1/beta/split/jobs` endpoint accepts only `file_id`.

    To use a Parse job as input, call `POST /api/v1/split/jobs` instead, where you
    can pass the Parse job ID as `file_input`.
    """

    value: str
    """Document identifier."""
