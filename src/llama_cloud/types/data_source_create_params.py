# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.cloud_s3_data_source import CloudS3DataSource
from .shared_params.cloud_box_data_source import CloudBoxDataSource
from .shared_params.cloud_jira_data_source import CloudJiraDataSource
from .shared_params.cloud_slack_data_source import CloudSlackDataSource
from .shared_params.cloud_jira_data_source_v2 import CloudJiraDataSourceV2
from .shared_params.cloud_one_drive_data_source import CloudOneDriveDataSource
from .shared_params.cloud_confluence_data_source import CloudConfluenceDataSource
from .shared_params.cloud_sharepoint_data_source import CloudSharepointDataSource
from .shared_params.cloud_notion_page_data_source import CloudNotionPageDataSource
from .shared_params.cloud_google_drive_data_source import CloudGoogleDriveDataSource
from .shared_params.cloud_az_storage_blob_data_source import CloudAzStorageBlobDataSource

__all__ = ["DataSourceCreateParams", "Component"]


class DataSourceCreateParams(TypedDict, total=False):
    component: Required[Component]
    """Component that implements the data source"""

    name: Required[str]
    """The name of the data source."""

    source_type: Required[
        Literal[
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
    ]

    organization_id: Optional[str]

    project_id: Optional[str]

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Custom metadata that will be present on all data loaded from the data source"""


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
