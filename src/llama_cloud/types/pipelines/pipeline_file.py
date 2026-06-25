# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PipelineFile"]


class PipelineFile(BaseModel):
    """A file associated with a pipeline."""

    id: str
    """Unique identifier for the pipeline file."""

    pipeline_id: str
    """The ID of the pipeline that the file is associated with."""

    config_hash: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Hashes for the configuration of the pipeline."""

    created_at: Optional[datetime] = None
    """When the pipeline file was created."""

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Custom metadata for the file."""

    data_source_id: Optional[str] = None
    """The ID of the data source that the file belongs to."""

    external_file_id: Optional[str] = None
    """The ID of the file in the external system."""

    file_id: Optional[str] = None
    """The ID of the file."""

    file_size: Optional[int] = None
    """Size of the file in bytes."""

    file_type: Optional[str] = None
    """File type (e.g. pdf, docx, etc.)."""

    indexed_page_count: Optional[int] = None
    """The number of pages that have been indexed for this file."""

    last_modified_at: Optional[datetime] = None
    """The last modified time of the file."""

    name: Optional[str] = None
    """Name of the file."""

    permission_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Permission information for the file."""

    project_id: Optional[str] = None
    """The ID of the project that the file belongs to."""

    resource_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Resource information for the file."""

    status: Optional[Literal["CANCELLED", "ERROR", "IN_PROGRESS", "NOT_STARTED", "SUCCESS"]] = None
    """Status of the pipeline file."""

    status_updated_at: Optional[datetime] = None
    """The last time the status was updated."""

    updated_at: Optional[datetime] = None
    """When the pipeline file was last updated."""
