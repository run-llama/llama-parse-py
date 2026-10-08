# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RetrievalFindParams"]


class RetrievalFindParams(TypedDict, total=False):
    index_id: Required[str]
    """ID of the index to search within."""

    organization_id: Optional[str]

    project_id: Optional[str]

    file_name: Optional[str]
    """Exact file name to match."""

    file_name_contains: Optional[str]
    """Substring match on file name (case-insensitive)."""

    page_size: Optional[int]
    """The maximum number of items to return.

    The service may return fewer than this value. If unspecified, a default page
    size will be used. The maximum value is typically 1000; values above this will
    be coerced to the maximum.
    """

    page_token: Optional[str]
    """A page token, received from a previous list call.

    Provide this to retrieve the subsequent page.
    """
