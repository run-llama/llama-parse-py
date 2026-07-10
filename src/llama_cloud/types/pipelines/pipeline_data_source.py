# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.cloud_s3_data_source import CloudS3DataSource
from ..shared.cloud_box_data_source import CloudBoxDataSource
from ..shared.cloud_jira_data_source import CloudJiraDataSource
from ..shared.cloud_slack_data_source import CloudSlackDataSource
from ..shared.cloud_jira_data_source_v2 import CloudJiraDataSourceV2
from ..shared.cloud_one_drive_data_source import CloudOneDriveDataSource
from ..data_source_reader_version_metadata import DataSourceReaderVersionMetadata
from ..shared.cloud_confluence_data_source import CloudConfluenceDataSource
from ..shared.cloud_sharepoint_data_source import CloudSharepointDataSource
from ..shared.cloud_notion_page_data_source import CloudNotionPageDataSource
from ..shared.cloud_google_drive_data_source import CloudGoogleDriveDataSource
from ..shared.cloud_az_storage_blob_data_source import CloudAzStorageBlobDataSource

__all__ = ["PipelineDataSource", "Component"]

Component: TypeAlias = Union[
    Dict[str, object],
    CloudS3DataSource,
    CloudAzStorageBlobDataSource,
    CloudGoogleDriveDataSource,
    CloudOneDriveDataSource,
    CloudSharepointDataSource,
    CloudSlackDataSource,
    CloudNotionPageDataSource,
    CloudConfluenceDataSource,
    CloudJiraDataSource,
    CloudJiraDataSourceV2,
    CloudBoxDataSource,
]


class PipelineDataSource(BaseModel):
    """Schema for a data source in a pipeline."""

    id: str
    """Unique identifier"""

    component: Component
    """Component that implements the data source"""

    data_source_id: str
    """The ID of the data source."""

    last_synced_at: datetime
    """The last time the data source was automatically synced."""

    name: str
    """The name of the data source."""

    pipeline_id: str
    """The ID of the pipeline."""

    project_id: str

    source_type: Literal[
        "AZURE_STORAGE_BLOB",
        "BOX",
        "CONFLUENCE",
        "GOOGLE_DRIVE",
        "JIRA",
        "JIRA_V2",
        "MICROSOFT_ONEDRIVE",
        "MICROSOFT_SHAREPOINT",
        "NOTION_PAGE",
        "S3",
        "SLACK",
    ]

    created_at: Optional[datetime] = None
    """Creation datetime"""

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Custom metadata that will be present on all data loaded from the data source"""

    status: Optional[Literal["CANCELLED", "ERROR", "IN_PROGRESS", "NOT_STARTED", "SUCCESS"]] = None
    """The status of the data source in the pipeline."""

    status_updated_at: Optional[datetime] = None
    """The last time the status was updated."""

    sync_interval: Optional[float] = None
    """The interval at which the data source should be synced."""

    sync_schedule_set_by: Optional[str] = None
    """The id of the user who set the sync schedule."""

    updated_at: Optional[datetime] = None
    """Update datetime"""

    version_metadata: Optional[DataSourceReaderVersionMetadata] = None
    """Version metadata for the data source"""
