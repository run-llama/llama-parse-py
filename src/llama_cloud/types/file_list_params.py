# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    expand: Optional[SequenceNotStr[str]]
    """Fields to expand on each file."""

    external_file_id: Optional[str]
    """Filter by external file ID."""

    file_ids: Optional[SequenceNotStr[str]]
    """Filter by specific file IDs."""

    file_name: Optional[str]
    """Filter by file name (exact match)."""

    order_by: Optional[str]
    """A comma-separated list of fields to order by, sorted in ascending order.

    Use 'field_name desc' to specify descending order.
    """

    organization_id: Optional[str]

    page_size: Optional[int]
    """The maximum number of items to return. Defaults to 50, maximum is 1000."""

    page_token: Optional[str]
    """A page token received from a previous list call.

    Provide this to retrieve the subsequent page.
    """

    project_id: Optional[str]
