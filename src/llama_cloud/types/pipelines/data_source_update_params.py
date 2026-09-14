# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DataSourceUpdateParams"]


class DataSourceUpdateParams(TypedDict, total=False):
    pipeline_id: Required[str]

    sync_interval: Optional[float]
    """The interval at which the data source should be synced."""
