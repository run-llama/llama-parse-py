# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudBoxDataSource"]


class CloudBoxDataSource(BaseModel):
    authentication_mechanism: Literal["ccg", "developer_token"]
    """The type of authentication to use (Developer Token or CCG)"""

    class_name: Optional[str] = None

    client_id: Optional[str] = None
    """
    Box API key used for identifying the application the user is authenticating with
    """

    enterprise_id: Optional[str] = None
    """Box Enterprise ID, if provided authenticates as service."""

    folder_id: Optional[str] = None
    """The ID of the Box folder to read from."""

    supports_access_control: Optional[bool] = None

    user_id: Optional[str] = None
    """Box User ID, if provided authenticates as user."""
