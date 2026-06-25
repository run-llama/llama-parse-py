# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DirectoryListResponse"]


class DirectoryListResponse(BaseModel):
    """API response schema for a directory."""

    id: str
    """Unique identifier for the directory."""

    name: str
    """Human-readable name for the directory."""

    project_id: str
    """Project the directory belongs to."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    deleted_at: Optional[datetime] = None
    """Optional timestamp of when the directory was deleted. Null if not deleted."""

    description: Optional[str] = None
    """Optional description shown to users."""

    expires_at: Optional[datetime] = None
    """When this directory expires and is eligible for cleanup."""

    system_metadata: Optional[Dict[str, object]] = None
    """Reserved system-managed metadata."""

    type: Optional[Literal["ephemeral", "index", "system_ephemeral", "user"]] = None
    """Directory type: 'user', 'index', 'ephemeral', or 'system_ephemeral'."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
