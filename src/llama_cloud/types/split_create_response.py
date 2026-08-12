# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .beta.split_category import SplitCategory
from .beta.split_result_response import SplitResultResponse

__all__ = ["SplitCreateResponse", "SplittingStrategy"]


class SplittingStrategy(BaseModel):
    """Strategy used for splitting."""

    allow_uncategorized: Optional[Literal["forbid", "include", "omit"]] = None
    """Controls handling of pages that don't match any category.

    'include': pages can be grouped as 'uncategorized' and included in results.
    'forbid': all pages must be assigned to a defined category. 'omit': pages can be
    classified as 'uncategorized' but are excluded from results.
    """


class SplitCreateResponse(BaseModel):
    """A split job."""

    id: str
    """Unique identifier for the split job."""

    categories: List[SplitCategory]
    """Categories used for splitting."""

    document_input_type: Literal["file_id", "parse_job_id", "url"]
    """Whether the input was a file or parse job"""

    file_input: str
    """File ID or parse job ID"""

    project_id: str
    """Project this job belongs to."""

    status: str
    """Current job status.

    Valid values are: pending, processing, completed, failed, cancelled.
    """

    user_id: str
    """User who created this job."""

    configuration_id: Optional[str] = None
    """Split configuration ID used for this job."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if the job failed."""

    result: Optional[SplitResultResponse] = None
    """Result of a completed split job."""

    splitting_strategy: Optional[SplittingStrategy] = None
    """Strategy used for splitting."""

    transaction_id: Optional[str] = None
    """Idempotency key scoped to the project, if one was provided."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
