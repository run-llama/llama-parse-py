# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .presigned_url import PresignedURL

__all__ = ["FileQueryResponse", "Item"]


class Item(BaseModel):
    """An uploaded file."""

    id: str
    """Unique file identifier"""

    name: str
    """File name including extension"""

    project_id: str
    """Project this file belongs to"""

    download_url: Optional[PresignedURL] = None
    """Schema for a presigned URL."""

    expires_at: Optional[datetime] = None
    """When the file expires and may be automatically removed.

    Null means no expiration.
    """

    external_file_id: Optional[str] = None
    """Optional ID for correlating with an external system"""

    file_type: Optional[str] = None
    """File extension (pdf, docx, png, etc.)"""

    last_modified_at: Optional[datetime] = None
    """When the file was last modified (ISO 8601)"""

    purpose: Optional[str] = None
    """
    How the file will be used: user_data, parse, extract, classify, split, sheet, or
    agent_app
    """


class FileQueryResponse(BaseModel):
    """Paginated list of files."""

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
