# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    directory_id: Required[str]

    organization_id: Optional[str]

    project_id: Optional[str]

    display_name: Optional[str]
    """Updated display name."""

    metadata: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], None]]]
    """User-defined metadata key-value pairs. Replaces the user metadata layer."""

    target_directory_id: Optional[str]
    """Move file to a different directory."""

    unique_id: Optional[str]
    """Updated unique identifier."""
