# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PipelineListPaginatedResponse"]


class PipelineListPaginatedResponse(BaseModel):
    """A pipeline in a project."""

    id: str
    """The pipeline's unique identifier."""

    name: str
    """The pipeline's display name."""

    pipeline_type: Literal["MANAGED", "PLAYGROUND"]
    """The pipeline's type."""

    project_id: str
    """The project the pipeline belongs to."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    status: Optional[Literal["CREATED", "DELETING"]] = None
    """The pipeline's current status."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
