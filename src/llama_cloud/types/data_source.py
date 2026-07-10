# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.cloud_s3_data_source import CloudS3DataSource
from .shared.cloud_box_data_source import CloudBoxDataSource
from .shared.cloud_jira_data_source import CloudJiraDataSource
from .shared.cloud_slack_data_source import CloudSlackDataSource
from .shared.cloud_jira_data_source_v2 import CloudJiraDataSourceV2
from .shared.cloud_one_drive_data_source import CloudOneDriveDataSource
from .data_source_reader_version_metadata import DataSourceReaderVersionMetadata
from .shared.cloud_confluence_data_source import CloudConfluenceDataSource
from .shared.cloud_sharepoint_data_source import CloudSharepointDataSource
from .shared.cloud_notion_page_data_source import CloudNotionPageDataSource
from .shared.cloud_google_drive_data_source import CloudGoogleDriveDataSource
from .shared.cloud_az_storage_blob_data_source import CloudAzStorageBlobDataSource

__all__ = ["DataSource", "Component"]

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


class DataSource(BaseModel):
    """Schema for a data source."""

    id: str
    """Unique identifier"""

    component: Component
    """Component that implements the data source"""

    name: str
    """The name of the data source."""

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

    updated_at: Optional[datetime] = None
    """Update datetime"""

    version_metadata: Optional[DataSourceReaderVersionMetadata] = None
    """Version metadata for the data source"""
