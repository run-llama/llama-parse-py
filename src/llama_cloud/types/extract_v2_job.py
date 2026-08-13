# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .extract_job_usage import ExtractJobUsage
from .extract_job_metadata import ExtractJobMetadata
from .extract_configuration import ExtractConfiguration

__all__ = ["ExtractV2Job", "Metadata"]


class Metadata(BaseModel):
    """Job-level metadata."""

    usage: Optional[ExtractJobUsage] = None
    """Extraction usage metrics."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ExtractV2Job(BaseModel):
    """An extraction job."""

    id: str
    """Unique job identifier (job_id)"""

    created_at: datetime
    """Creation timestamp"""

    file_input: str
    """File ID or parse job ID that was extracted"""

    project_id: str
    """Project this job belongs to"""

    status: str
    """Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user
    """

    updated_at: datetime
    """Last update timestamp"""

    configuration: Optional[ExtractConfiguration] = None
    """Extract configuration combining parse and extract settings."""

    configuration_id: Optional[str] = None
    """Saved extract configuration ID used for this job, if any"""

    error_message: Optional[str] = None
    """Error details when status is FAILED"""

    extract_metadata: Optional[ExtractJobMetadata] = None
    """Extraction metadata."""

    extract_result: Union[
        Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]],
        List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]],
        None,
    ] = None
    """Extracted data conforming to the data_schema.

    Returns a single object for per_doc, or an array for per_page / per_table_row.
    """

    metadata: Optional[Metadata] = None
    """Job-level metadata."""
