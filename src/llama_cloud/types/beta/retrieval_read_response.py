# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RetrievalReadResponse"]


class RetrievalReadResponse(BaseModel):
    """File read result."""

    content: str
    """Parsed text content of the file."""
