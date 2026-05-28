# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BatchCreateResponse", "Config", "ConfigJob", "Result", "ResultJobReference"]


class ConfigJob(BaseModel):
    """Job to create for each file in the source directory."""

    configuration_id: str
    """Product configuration ID or built-in preset ID matching the job type."""

    type: Literal["parse_v2", "extract_v2"]
    """Product job type to run for each source directory file."""


class Config(BaseModel):
    """Batch configuration snapshot."""

    job: ConfigJob
    """Job to create for each file in the source directory."""


class ResultJobReference(BaseModel):
    """Reference to a job produced by a batch.

    Example:
        {
            "type": "parse_v2",
            "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        }
    """

    id: str
    """Job ID, such as a parse job ID."""

    type: Literal["parse_v2", "extract_v2"]
    """Type of job produced for the file."""


class Result(BaseModel):
    """Result projection for one source directory file in a batch.

    Example:
        {
            "source_directory_file_id": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            "job_reference": {
                "type": "parse_v2",
                "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
            },
            "error_message": null
        }

    This is a projection of directory-sync state, not a separate child
    resource that callers need to create. The source directory file ID is the
    stable correlation key. Underlying job progress and failures should be
    resolved through the referenced product job endpoint.
    """

    source_directory_file_id: str
    """Source directory file processed by this batch."""

    error_message: Optional[str] = None
    """
    Batch-level mapping error if the system could not create or associate a job for
    this source file.
    """

    job_reference: Optional[ResultJobReference] = None
    """Reference to a job produced by a batch.

    Example: { "type": "parse_v2", "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    }
    """


class BatchCreateResponse(BaseModel):
    """A top-level batch.

    Example:
        {
            "id": "bat-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            "source_directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            "config": {
                "job": {
                    "type": "parse_v2",
                    "configuration_id": "cfg-PARSE_AGENTIC"
                }
            },
            "status": "COMPLETED",
            "results": [
                {
                    "source_directory_file_id": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "job_reference": {
                        "type": "parse_v2",
                        "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
                    },
                    "error_message": null
                }
            ]
        }

    Batch-level ``FAILED`` means the orchestration failed and cannot provide a
    reliable per-file result set. ``results`` is only populated when explicitly
    requested with ``expand=results`` and may be ``null`` while a batch is still
    running.
    """

    id: str
    """Unique identifier"""

    config: Config
    """Batch configuration snapshot."""

    project_id: str
    """Project this batch belongs to."""

    source_directory_id: str
    """Directory being processed."""

    status: Literal["PENDING", "THROTTLED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """Current batch status."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    results: Optional[List[Result]] = None
    """Expanded per-file result mappings.

    Null unless requested with expand=results, or while the batch is still running.
    """

    updated_at: Optional[datetime] = None
    """Update datetime"""
