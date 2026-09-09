# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["SheetGetParams"]


class SheetGetParams(TypedDict, total=False):
    expand: SequenceNotStr[str]
    """Optional fields to populate on the response.

    Valid values: metadata_state_transitions.
    """

    include_results: bool

    organization_id: Optional[str]

    project_id: Optional[str]
