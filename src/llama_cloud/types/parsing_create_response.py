# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParsingCreateResponse"]


class ParsingCreateResponse(BaseModel):
    """A parse job."""

    id: str
    """Unique parse job identifier"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
    """Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error details when status is FAILED"""

    name: Optional[str] = None
    """Optional display name for this parse job"""

    tier: Optional[str] = None
    """Parsing tier used for this job"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
