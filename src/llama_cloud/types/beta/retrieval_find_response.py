# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RetrievalFindResponse"]


class RetrievalFindResponse(BaseModel):
    """A file returned by find."""

    file_id: str
    """ID of the file."""

    file_name: str
    """Display name of the file."""
