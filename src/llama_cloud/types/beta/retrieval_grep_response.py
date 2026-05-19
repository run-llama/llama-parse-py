# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["RetrievalGrepResponse", "Match"]


class Match(BaseModel):
    """A single grep match within a file."""

    content: str
    """Matched text content."""

    end_char: int
    """End character offset of the match."""

    start_char: int
    """Start character offset of the match."""


class RetrievalGrepResponse(BaseModel):
    """Grep results for a file."""

    matches: List[Match]
    """Regex matches found in the file."""
