# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RetrievalGrepParams"]


class RetrievalGrepParams(TypedDict, total=False):
    file_id: Required[str]
    """ID of the file to grep."""

    index_id: Required[str]
    """ID of the index the file belongs to."""

    pattern: Required[str]
    """Regex pattern to search for."""

    organization_id: Optional[str]

    project_id: Optional[str]

    context_chars: Optional[int]
    """
    Number of characters of context to include before and after the matched pattern
    in the content field of the response
    """

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
