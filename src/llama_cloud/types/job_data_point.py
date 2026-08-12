# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["JobDataPoint", "StateTransitions"]


class StateTransitions(BaseModel):
    """Job state transition timestamps."""

    cancelled_at: Optional[datetime] = None

    completed_at: Optional[datetime] = None

    failed_at: Optional[datetime] = None

    pending_at: Optional[datetime] = None

    running_at: Optional[datetime] = None

    throttled_at: Optional[datetime] = None


class JobDataPoint(BaseModel):
    """A job data point."""

    id: str
    """Job ID."""

    created_at: datetime
    """Created timestamp."""

    custom_tag: str
    """Custom tag."""

    project_id: str
    """Project ID."""

    status: str
    """Job status."""

    updated_at: datetime
    """Updated timestamp."""

    error_message: Optional[str] = None
    """Error message, if any."""

    state_transitions: Optional[StateTransitions] = None
    """Job state transition timestamps."""
