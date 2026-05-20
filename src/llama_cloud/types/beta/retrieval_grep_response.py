# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RetrievalGrepResponse"]


class RetrievalGrepResponse(BaseModel):
    """A single grep match within a file."""

    content: str
    """Matched text content."""

    end_char: int
    """End character offset of the match."""

    start_char: int
    """Start character offset of the match."""
