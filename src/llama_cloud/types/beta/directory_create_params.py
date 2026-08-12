# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DirectoryCreateParams"]


class DirectoryCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name for the directory."""

    organization_id: Optional[str]

    project_id: Optional[str]

    connector_subscription_id: Optional[str]
    """Connector Subscription whose files sync into this directory.

    Omit for manual uploads.
    """

    description: Optional[str]
    """Optional description shown to users."""

    system_metadata: Optional[Dict[str, object]]
    """Reserved system-managed metadata."""

    type: Literal["ephemeral", "user"]
    """Directory type. Use 'ephemeral' for batch processing with automatic cleanup."""
