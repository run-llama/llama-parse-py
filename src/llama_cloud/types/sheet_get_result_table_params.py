# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SheetGetResultTableParams"]


class SheetGetResultTableParams(TypedDict, total=False):
    spreadsheet_job_id: Required[str]

    region_id: Required[str]

    expires_at_seconds: Optional[int]

    organization_id: Optional[str]

    project_id: Optional[str]
