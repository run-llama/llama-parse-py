# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    upload_file: Required[FileTypes]

    organization_id: Optional[str]

    project_id: Optional[str]

    display_name: Optional[str]

    external_file_id: Optional[str]

    metadata: Optional[str]
    """User metadata as a JSON object string."""

    unique_id: Optional[str]
