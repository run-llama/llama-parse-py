# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ManagedIngestionStatusResponse", "Error"]


class Error(BaseModel):
    job_id: str
    """ID of the job that failed."""

    message: str
    """List of errors that occurred during ingestion."""

    step: Literal[
        "DATA_SOURCE", "FILE_UPDATER", "INGESTION", "MANAGED_INGESTION", "METADATA_UPDATE", "PARSE", "TRANSFORM"
    ]
    """Name of the job that failed."""


class ManagedIngestionStatusResponse(BaseModel):
    status: Literal["CANCELLED", "ERROR", "IN_PROGRESS", "NOT_STARTED", "PARTIAL_SUCCESS", "SUCCESS"]
    """Status of the ingestion."""

    deployment_date: Optional[datetime] = None
    """Date of the deployment."""

    effective_at: Optional[datetime] = None
    """When the status is effective"""

    error: Optional[List[Error]] = None
    """List of errors that occurred during ingestion."""

    job_id: Optional[str] = None
    """ID of the latest job."""
