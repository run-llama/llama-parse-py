# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["CloudGoogleDriveDataSource"]


class CloudGoogleDriveDataSource(BaseModel):
    folder_id: str
    """The ID of the Google Drive folder to read from."""

    class_name: Optional[str] = None

    folder_name: Optional[str] = None
    """Human-readable name of the selected folder, for display."""

    service_account_key: Optional[Dict[str, str]] = None
    """A dictionary containing secret values"""

    supports_access_control: Optional[bool] = None
