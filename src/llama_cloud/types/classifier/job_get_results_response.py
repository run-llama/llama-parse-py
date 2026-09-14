# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["JobGetResultsResponse", "Item", "ItemResult"]


class ItemResult(BaseModel):
    """Result of classifying a single file."""

    confidence: float
    """Confidence score of the classification (0.0-1.0)"""

    reasoning: str
    """
    Step-by-step explanation of why this classification was chosen and the
    confidence score assigned
    """

    type: Optional[str] = None
    """The document type that best matches, or null if no match."""


class Item(BaseModel):
    """A file classification."""

    id: str
    """Unique identifier"""

    classify_job_id: str
    """The ID of the classify job"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    file_id: Optional[str] = None
    """The ID of the classified file"""

    result: Optional[ItemResult] = None
    """Result of classifying a single file."""

    updated_at: Optional[datetime] = None
    """Update datetime"""


class JobGetResultsResponse(BaseModel):
    """Response model for the classify endpoint following AIP-132 pagination standard."""

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
