# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DataSourceUpdateDataSourcesParams", "Body"]


class DataSourceUpdateDataSourcesParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    """Schema for creating an association between a data source and a pipeline."""

    data_source_id: Required[str]
    """The ID of the data source."""

    sync_interval: Optional[float]
    """The interval at which the data source should be synced.

    Valid values are: 21600, 43200, 86400
    """
