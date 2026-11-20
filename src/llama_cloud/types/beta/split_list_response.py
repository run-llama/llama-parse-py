# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .split_category import SplitCategory
from .split_document_input import SplitDocumentInput
from .split_result_response import SplitResultResponse

__all__ = ["SplitListResponse"]


class SplitListResponse(BaseModel):
    """Beta response — uses nested document_input object."""

    id: str
    """Unique identifier for the split job."""

    categories: List[SplitCategory]
    """Categories used for splitting."""

    document_input: SplitDocumentInput
    """Document that was split."""

    project_id: str
    """Project ID this job belongs to."""

    status: str
    """Current status of the job.

    Valid values are: pending, processing, completed, failed, cancelled.
    """

    user_id: str
    """User ID who created this job."""

    version: str
    """Split version used for this job."""

    configuration_id: Optional[str] = None
    """Split configuration ID used for this job."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if the job failed."""

    result: Optional[SplitResultResponse] = None
    """Result of a completed split job."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
