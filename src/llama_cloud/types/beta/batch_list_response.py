# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BatchListResponse"]


class BatchListResponse(BaseModel):
    """Response schema for a batch processing job."""

    id: str
    """Unique identifier for the batch job"""

    job_type: Literal["classify", "extract", "parse"]
    """Type of processing operation (parse or classify)"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["cancelled", "completed", "dispatched", "failed", "pending", "running"]
    """Current job status"""

    total_items: int
    """Total number of items in the job"""

    completed_at: Optional[datetime] = None
    """Timestamp when job completed"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    directory_id: Optional[str] = None
    """Directory being processed"""

    effective_at: Optional[datetime] = None

    error_message: Optional[str] = None
    """Error message for the latest job attempt, if any."""

    failed_items: Optional[int] = None
    """Number of items that failed processing"""

    job_record_id: Optional[str] = None
    """The job record ID associated with this status, if any."""

    processed_items: Optional[int] = None
    """Number of items processed so far"""

    skipped_items: Optional[int] = None
    """Number of items skipped (already processed or size limit)"""

    started_at: Optional[datetime] = None
    """Timestamp when job processing started"""

    updated_at: Optional[datetime] = None
    """Update datetime"""

    workflow_id: Optional[str] = None
    """Async job tracking ID"""
