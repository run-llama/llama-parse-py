# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    """Schema for a project."""

    id: str
    """Unique identifier"""

    name: str

    organization_id: str
    """The Organization ID the project is under."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    is_default: Optional[bool] = None
    """Whether this project is the default project for the user."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
