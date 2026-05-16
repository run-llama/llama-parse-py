# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    path_directory_id: Required[Annotated[str, PropertyInfo(alias="directory_id")]]

    organization_id: Optional[str]

    project_id: Optional[str]

    body_directory_id: Annotated[Optional[str], PropertyInfo(alias="directory_id")]
    """Move file to a different directory."""

    display_name: Optional[str]
    """Updated display name."""

    metadata: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], None]]]
    """User-defined metadata key-value pairs. Replaces the user metadata layer."""

    unique_id: Optional[str]
    """Updated unique identifier."""
