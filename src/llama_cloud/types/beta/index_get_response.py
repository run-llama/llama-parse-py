# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["IndexGetResponse"]


class IndexGetResponse(BaseModel):
    """A searchable index over a directory of documents."""

    id: str
    """Unique identifier"""

    export_config_id: str
    """ID of the export configuration."""

    name: str
    """Index name."""

    project_id: str
    """Project this index belongs to."""

    source_directory_id: str
    """ID of the source directory."""

    sync_config_id: str
    """ID of the sync configuration."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    description: Optional[str] = None
    """Index description."""

    last_exported_at: Optional[datetime] = None
    """Last export time."""

    last_synced_at: Optional[datetime] = None
    """Last sync time."""

    metadata: Optional[Dict[str, object]] = None
    """Build state and diagnostic info."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
