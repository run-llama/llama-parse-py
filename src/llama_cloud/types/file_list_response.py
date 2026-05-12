# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .presigned_url import PresignedURL

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
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
