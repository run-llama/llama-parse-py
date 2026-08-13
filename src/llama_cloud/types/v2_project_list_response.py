# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["V2ProjectListResponse"]


class V2ProjectListResponse(BaseModel):
    """API response schema for a project."""

    id: str
    """The project's unique identifier."""

    name: str
    """The project's display name."""

    organization_id: str
    """The organization the project belongs to."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    is_default: Optional[bool] = None
    """Whether this project is the default project for its organization."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
