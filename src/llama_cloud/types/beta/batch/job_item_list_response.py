# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["JobItemListResponse"]


class JobItemListResponse(BaseModel):
    """Detailed information about an item in a batch job."""

    item_id: str
    """ID of the item"""

    item_name: str
    """Name of the item"""

    status: Literal["cancelled", "completed", "failed", "pending", "processing", "skipped"]
    """Processing status of this item"""

    completed_at: Optional[datetime] = None
    """When processing completed for this item"""

    effective_at: Optional[datetime] = None

    error_message: Optional[str] = None
    """Error message for the latest job attempt, if any."""

    job_id: Optional[str] = None
    """Job ID for the underlying processing job (links to parse/extract job results)"""

    job_record_id: Optional[str] = None
    """The job record ID associated with this status, if any."""

    skip_reason: Optional[str] = None
    """Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')"""

    started_at: Optional[datetime] = None
    """When processing started for this item"""
