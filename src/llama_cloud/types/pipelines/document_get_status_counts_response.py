# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["DocumentGetStatusCountsResponse"]


class DocumentGetStatusCountsResponse(BaseModel):
    """Counts of the documents in a pipeline, grouped by ingestion status."""

    counts: Dict[str, int]
    """Number of documents per ingestion status; every status is present."""

    pipeline_id: str
    """ID of the pipeline the documents belong to."""

    total_count: int
    """Total number of documents counted."""

    data_source_id: Optional[str] = None
    """Data source the counts were restricted to."""

    file_id: Optional[str] = None
    """File the counts were restricted to."""

    only_direct_upload: Optional[bool] = None
    """Whether only directly uploaded documents were counted."""
