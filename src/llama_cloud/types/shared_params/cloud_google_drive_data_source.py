# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudGoogleDriveDataSource"]


class CloudGoogleDriveDataSource(TypedDict, total=False):
    folder_id: Required[str]
    """The ID of the Google Drive folder to read from."""

    class_name: str

    folder_name: Optional[str]
    """Human-readable name of the selected folder, for display."""

    service_account_key: Optional[Dict[str, str]]
    """A dictionary containing secret values"""

    supports_access_control: bool
