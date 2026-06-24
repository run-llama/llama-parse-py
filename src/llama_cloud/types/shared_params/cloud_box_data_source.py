# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudBoxDataSource"]


class CloudBoxDataSource(TypedDict, total=False):
    authentication_mechanism: Required[Literal["ccg", "developer_token"]]
    """The type of authentication to use (Developer Token or CCG)"""

    class_name: str

    client_id: Optional[str]
    """
    Box API key used for identifying the application the user is authenticating with
    """

    client_secret: Optional[str]
    """Box API secret used for making auth requests."""

    developer_token: Optional[str]
    """
    Developer token for authentication if authentication_mechanism is
    'developer_token'.
    """

    enterprise_id: Optional[str]
    """Box Enterprise ID, if provided authenticates as service."""

    folder_id: Optional[str]
    """The ID of the Box folder to read from."""

    supports_access_control: bool

    user_id: Optional[str]
    """Box User ID, if provided authenticates as user."""
