# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ExtractDeleteParams"]


class ExtractDeleteParams(TypedDict, total=False):
    force: bool

    organization_id: Optional[str]

    project_id: Optional[str]
