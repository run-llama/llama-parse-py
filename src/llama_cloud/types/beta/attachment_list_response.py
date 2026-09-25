# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AttachmentListResponse"]


class AttachmentListResponse(BaseModel):
    """Metadata for a single file attachment."""

    name: str
    """Name of the attachment"""

    size: int
    """Size of the attachment in bytes"""

    last_modified: Optional[datetime] = None
    """When the attachment was last modified"""
