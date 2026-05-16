# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from ...._models import BaseModel
from ...presigned_url import PresignedURL

__all__ = ["FileGetResponse"]


class FileGetResponse(BaseModel):
    """API response schema for a directory file."""

    id: str
    """Unique identifier for the directory file."""

    directory_id: str
    """Directory the file belongs to."""

    display_name: str
    """Display name for the file."""

    project_id: str
    """Project the directory file belongs to."""

    unique_id: str
    """Unique identifier for the file in the directory"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    deleted_at: Optional[datetime] = None
    """Soft delete marker when the file is removed upstream or by user action."""

    download_url: Optional[PresignedURL] = None
    """Schema for a presigned URL."""

    file_id: Optional[str] = None
    """File ID for the storage location."""

    metadata: Optional[Dict[str, Union[str, float, bool, List[str], None]]] = None
    """Merged metadata from all sources. Higher-priority sources override lower."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
