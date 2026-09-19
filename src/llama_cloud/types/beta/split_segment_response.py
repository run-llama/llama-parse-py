# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["SplitSegmentResponse"]


class SplitSegmentResponse(BaseModel):
    """A segment of the split document."""

    category: str
    """Category name this split belongs to."""

    confidence_category: str
    """Categorical confidence level. Valid values are: high, medium, low."""

    pages: List[int]
    """Page numbers in this segment, as numbered by the input document."""
