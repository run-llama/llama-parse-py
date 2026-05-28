# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BBox"]


class BBox(BaseModel):
    """Bounding box with coordinates and optional metadata."""

    h: float
    """Height of the bounding box"""

    w: float
    """Width of the bounding box"""

    x: float
    """X coordinate of the bounding box"""

    y: float
    """Y coordinate of the bounding box"""

    confidence: Optional[float] = None
    """Confidence score"""

    end_index: Optional[int] = None
    """End index in the text"""

    label: Optional[str] = None
    """Label for the bounding box"""

    r: Optional[float] = None
    """Optional visual text rotation angle in degrees. Omitted when unrotated."""

    start_index: Optional[int] = None
    """Start index in the text"""
