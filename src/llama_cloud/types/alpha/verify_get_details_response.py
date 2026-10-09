# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VerifyGetDetailsResponse", "DegradedTool", "Evidence", "Heatmap", "PageDimension", "Region"]


class DegradedTool(BaseModel):
    """A check that was attempted but could not run on this job."""

    tool: str
    """Name of the check"""

    reason: Optional[str] = None
    """Why the check could not run"""


class Evidence(BaseModel):
    """A single piece of evidence produced by a detection tool."""

    code: str
    """Machine-readable evidence code"""

    detail: str
    """Human-readable evidence detail"""

    family: str
    """Signal family (e.g. metadata, splicing, compression)"""

    score: float
    """Evidence strength score"""

    tool: str
    """Tool that produced this evidence"""

    data: Optional[Dict[str, object]] = None
    """Tool-specific structured payload"""

    hard: Optional[bool] = None
    """Whether this is hard (conclusive) evidence"""


class Heatmap(BaseModel):
    """A per-page forensic heatmap overlay, as a presigned image URL."""

    expires_at: datetime
    """The time at which the presigned URL expires"""

    kind: str
    """Producing signal, e.g. double_compression, ela, noise"""

    page: int
    """0-based page index (0 for standalone images)"""

    url: str
    """Presigned URL to the heatmap PNG (page overlay)"""

    score: Optional[float] = None
    """Producing tool's max score (for ranking)"""


class PageDimension(BaseModel):
    """
    Rendered pixel size of a page — the coordinate space region bboxes use,
    so the UI can scale the suspect-region overlay onto the displayed page.
    """

    height: int
    """Rendered page height in pixels"""

    page: int
    """0-based page index (0 for standalone images)"""

    width: int
    """Rendered page width in pixels"""


class Region(BaseModel):
    """A suspicious region localized on a rendered page."""

    bbox: List[int]
    """Region bounding box as [x, y, w, h] in page-render pixels"""

    detail: str
    """Human-readable detail about the region"""

    kind: str
    """Kind of anomaly detected in this region"""

    page: int
    """0-based page index (0 for standalone images)"""

    score: float
    """Region-level doctoring likelihood score"""

    source: str
    """Detector/tool that produced this region"""

    primary: Optional[bool] = None
    """
    Whether this region is part of the small set of decisive evidence behind the
    verdict — the boxes a reviewer should look at first
    """

    review: Optional[str] = None
    """Review status/verdict for this region"""

    review_note: Optional[str] = None
    """Free-form review note for this region"""


class VerifyGetDetailsResponse(BaseModel):
    """Raw per-signal detail for a completed Verify job.

    Forensic drill-down behind the simplified result: the full evidence list,
    per-family sub-scores, raw localized regions, and heatmap overlays.
    """

    job_id: str
    """ID of the Verify job"""

    degraded_tools: Optional[List[DegradedTool]] = None
    """Checks that could not run on this job (with the reason).

    A check listed here produced no findings because it could not run, not because
    the document is clean
    """

    evidence: Optional[List[Evidence]] = None
    """Evidence items produced by detection tools"""

    heatmaps: Optional[List[Heatmap]] = None
    """Per-page forensic heatmap overlays as presigned image URLs"""

    page_dimensions: Optional[List[PageDimension]] = None
    """Rendered pixel size per page, so region bboxes can be scaled onto the page"""

    regions: Optional[List[Region]] = None
    """Suspicious regions localized on rendered pages"""

    sub_scores: Optional[Dict[str, float]] = None
    """
    Per-family scores (metadata, ai_generation, splicing, copy_move, compression,
    noise, coherence, pdf_structure)
    """
