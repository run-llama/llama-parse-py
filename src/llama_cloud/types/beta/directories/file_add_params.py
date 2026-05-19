# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FileAddParams"]


class FileAddParams(TypedDict, total=False):
    file_id: Required[str]
    """File ID for the storage location (required)."""

    organization_id: Optional[str]

    project_id: Optional[str]

    display_name: Optional[str]
    """Display name for the file. If not provided, will use the file's name."""

    metadata: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], None]]]
    """User-defined metadata key-value pairs to associate with the file."""

    unique_id: Optional[str]
    """Unique identifier for the file in the directory.

    If not provided, will use the file's external_file_id or name.
    """
