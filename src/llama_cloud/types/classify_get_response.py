# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .classify_result import ClassifyResult
from .classify_configuration import ClassifyConfiguration

__all__ = ["ClassifyGetResponse"]


class ClassifyGetResponse(BaseModel):
    """Response for a classify job."""

    id: str
    """Unique identifier"""

    configuration: ClassifyConfiguration
    """Classify configuration used for this job"""

    document_input_type: Literal["file_id", "parse_job_id", "url"]
    """Whether the input was a file or parse job (FILE or PARSE_JOB)"""

    file_input: str
    """ID of the input file or parse job"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
    """Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED"""

    user_id: str
    """User who created this job"""

    configuration_id: Optional[str] = None
    """Product configuration ID"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    parse_job_id: Optional[str] = None
    """Associated parse job ID"""

    result: Optional[ClassifyResult] = None
    """Result of classifying a document."""

    transaction_id: Optional[str] = None
    """Idempotency key"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
