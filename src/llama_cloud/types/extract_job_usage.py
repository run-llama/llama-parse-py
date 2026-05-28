# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExtractJobUsage"]


class ExtractJobUsage(BaseModel):
    """Extraction usage metrics."""

    num_pages_extracted: Optional[int] = None
    """Number of pages extracted"""
