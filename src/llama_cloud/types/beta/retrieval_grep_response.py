# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RetrievalGrepResponse", "Item"]


class Item(BaseModel):
    """A single grep match within a file."""

    content: str
    """Matched text content."""

    end_char: int
    """End character offset of the match."""

    start_char: int
    """Start character offset of the match."""


class RetrievalGrepResponse(BaseModel):
    """Paginated grep results for a file."""

    items: List[Item]
    """The list of items."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page.

    If this field is omitted, there are no subsequent pages.
    """

    total_size: Optional[int] = None
    """The total number of items available.

    This is only populated when specifically requested. The value may be an estimate
    and can be used for display purposes only.
    """
