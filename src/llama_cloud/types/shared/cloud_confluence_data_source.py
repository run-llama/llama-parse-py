# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .failure_handling_config import FailureHandlingConfig

__all__ = ["CloudConfluenceDataSource"]


class CloudConfluenceDataSource(BaseModel):
    authentication_mechanism: str
    """Type of Authentication for connecting to Confluence APIs."""

    server_url: str
    """The server URL of the Confluence instance."""

    class_name: Optional[str] = None

    cql: Optional[str] = None
    """The CQL query to use for fetching pages."""

    failure_handling: Optional[FailureHandlingConfig] = None
    """Configuration for handling failures during processing.

    Key-value object controlling failure handling behaviors.

    Example: { "skip_list_failures": true }

    Currently supports:

    - skip_list_failures: Skip failed batches/lists and continue processing
    """

    index_restricted_pages: Optional[bool] = None
    """Whether to index restricted pages."""

    keep_markdown_format: Optional[bool] = None
    """Whether to keep the markdown format."""

    label: Optional[str] = None
    """The label to use for fetching pages."""

    page_ids: Optional[str] = None
    """The page IDs of the Confluence to read from."""

    space_key: Optional[str] = None
    """The space key to read from."""

    supports_access_control: Optional[bool] = None

    sync_permissions: Optional[bool] = None
    """
    Whether to fetch space-level permissions (allowed users/groups) and attach them
    to document metadata for access control. Disable for Confluence Server/Data
    Center versions whose permission APIs are unavailable (e.g. the JSON-RPC API
    removed in Data Center 9.2.6+), which otherwise surface as 401 errors during
    sync.
    """

    user_name: Optional[str] = None
    """The username to use for authentication."""
