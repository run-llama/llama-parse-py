# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BatchCancelResponse"]


class BatchCancelResponse(BaseModel):
    """Response after cancelling a batch job."""

    job_id: str
    """ID of the cancelled job"""

    message: str
    """Confirmation message"""

    processed_items: int
    """Number of items processed before cancellation"""

    status: Literal["cancelled", "completed", "dispatched", "failed", "pending", "running"]
    """New status (should be 'cancelled')"""
