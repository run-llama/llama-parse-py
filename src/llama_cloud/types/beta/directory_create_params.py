# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DirectoryCreateParams"]


class DirectoryCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name for the directory."""

    organization_id: Optional[str]

    project_id: Optional[str]

    description: Optional[str]
    """Optional description shown to users."""
