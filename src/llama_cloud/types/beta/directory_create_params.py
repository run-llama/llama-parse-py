# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DirectoryCreateParams"]


class DirectoryCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name for the directory."""

    organization_id: Optional[str]

    project_id: Optional[str]

    description: Optional[str]
    """Optional description shown to users."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When this directory expires. Required for ephemeral directories."""

    system_metadata: Optional[Dict[str, object]]
    """Reserved system-managed metadata."""

    type: Literal["user", "ephemeral"]
    """Directory type. Use 'ephemeral' for batch processing with automatic cleanup."""
