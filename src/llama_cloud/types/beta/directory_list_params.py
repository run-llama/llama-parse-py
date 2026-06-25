# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DirectoryListParams"]


class DirectoryListParams(TypedDict, total=False):
    include_deleted: bool
    """Include deleted directories."""

    name: Optional[str]
    """Directory name to match."""

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]

    type: Optional[Literal["ephemeral", "index", "user"]]
    """Directory type to include."""

    types: Optional[List[Literal["ephemeral", "index", "user"]]]
    """Filter by one or more directory types.

    Repeat the parameter for multiple values.
    """
