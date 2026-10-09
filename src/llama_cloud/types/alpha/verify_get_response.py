# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "VerifyGetResponse",
    "Configuration",
    "Result",
    "ResultCompositeScores",
    "ResultCompositeScoresAIGenerated",
    "ResultCompositeScoresDocumentCoherence",
    "ResultCompositeScoresDocumentMetadata",
    "ResultCompositeScoresKnownFraud",
    "ResultCompositeScoresManuallyEdited",
    "ResultCompositeScoresRecapture",
    "ResultPageDimension",
    "ResultSuspectRegion",
]


class Configuration(BaseModel):
    """Verify configuration used for this job"""

    target_pages: Optional[str] = None
    """Comma-separated page numbers or ranges to analyze (1-based).

    Omit to analyze all pages. Ignored for non-PDF inputs.
    """

    tier: Optional[Literal["agentic", "fast"]] = None
    """
    Verify tier: 'fast' runs only the quick deterministic forensic checks (metadata,
    content integrity, container structure, pixel statistics); 'agentic' (default)
    runs the full pipeline including the learned detectors and the semantic review
    pass.
    """


class ResultCompositeScoresAIGenerated(BaseModel):
    """Was this content synthesized by a generative model?"""

    applicable: Optional[bool] = None
    """Whether the checks feeding this composite ran on this document.

    When false the document was not checked for this — not cleared of it
    """

    score: Optional[float] = None
    """Score (0 to 1); null when the composite was not applicable"""


class ResultCompositeScoresDocumentCoherence(BaseModel):
    """
    Does the document's content agree with itself (checksums, arithmetic, machine-readable zones)?
    """

    applicable: Optional[bool] = None
    """Whether the checks feeding this composite ran on this document.

    When false the document was not checked for this — not cleared of it
    """

    score: Optional[float] = None
    """Score (0 to 1); null when the composite was not applicable"""


class ResultCompositeScoresDocumentMetadata(BaseModel):
    """
    Does the file's provenance / toolchain history look suspicious? Advisory: individually weak workflow-hygiene signals
    """

    applicable: Optional[bool] = None
    """Whether the checks feeding this composite ran on this document.

    When false the document was not checked for this — not cleared of it
    """

    score: Optional[float] = None
    """Score (0 to 1); null when the composite was not applicable"""


class ResultCompositeScoresKnownFraud(BaseModel):
    """Has this asset (or its template) been seen in fraud before?"""

    applicable: Optional[bool] = None
    """Whether the checks feeding this composite ran on this document.

    When false the document was not checked for this — not cleared of it
    """

    score: Optional[float] = None
    """Score (0 to 1); null when the composite was not applicable"""


class ResultCompositeScoresManuallyEdited(BaseModel):
    """Was this document altered after creation (splice, retype, redact, inpaint)?"""

    applicable: Optional[bool] = None
    """Whether the checks feeding this composite ran on this document.

    When false the document was not checked for this — not cleared of it
    """

    score: Optional[float] = None
    """Score (0 to 1); null when the composite was not applicable"""


class ResultCompositeScoresRecapture(BaseModel):
    """
    Was the document captured through a channel that destroys forensic evidence (photo of a screen, print-then-rescan)?
    """

    applicable: Optional[bool] = None
    """Whether the checks feeding this composite ran on this document.

    When false the document was not checked for this — not cleared of it
    """

    score: Optional[float] = None
    """Score (0 to 1); null when the composite was not applicable"""


class ResultCompositeScores(BaseModel):
    """Composite scores, each answering one question about the document"""

    ai_generated: Optional[ResultCompositeScoresAIGenerated] = None
    """Was this content synthesized by a generative model?"""

    document_coherence: Optional[ResultCompositeScoresDocumentCoherence] = None
    """
    Does the document's content agree with itself (checksums, arithmetic,
    machine-readable zones)?
    """

    document_metadata: Optional[ResultCompositeScoresDocumentMetadata] = None
    """
    Does the file's provenance / toolchain history look suspicious? Advisory:
    individually weak workflow-hygiene signals
    """

    known_fraud: Optional[ResultCompositeScoresKnownFraud] = None
    """Has this asset (or its template) been seen in fraud before?"""

    manually_edited: Optional[ResultCompositeScoresManuallyEdited] = None
    """Was this document altered after creation (splice, retype, redact, inpaint)?"""

    recapture: Optional[ResultCompositeScoresRecapture] = None
    """
    Was the document captured through a channel that destroys forensic evidence
    (photo of a screen, print-then-rescan)?
    """


class ResultPageDimension(BaseModel):
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


class ResultSuspectRegion(BaseModel):
    """A region that led to the suspected fraud, with why it is suspect.

    A curated, high-signal subset of ``regions``: reviewer-dismissed candidates
    are dropped and the remainder is ranked by suspicion, so consumers can act
    on ``verdict`` + ``confidence`` + this list without reading the raw signals.
    """

    bbox: List[int]
    """Region bounding box as [x, y, w, h] in page-render pixels"""

    explanation: str
    """Human-readable explanation of what makes this region suspect"""

    kind: str
    """Kind of anomaly detected in this region"""

    page: int
    """0-based page index (0 for standalone images)"""

    score: float
    """Suspicion score for this region (0 to 1)"""

    source: str
    """Detector that flagged this region"""

    primary: Optional[bool] = None
    """
    Whether this region is part of the small set of decisive evidence behind the
    verdict — the boxes a reviewer should look at first
    """

    review: Optional[str] = None
    """
    Automated reviewer verdict for this region (confirmed, dismissed, unsure, or
    empty). A dismissed region can still be surfaced when it is the only place to
    look; this label says how to read it
    """


class Result(BaseModel):
    """Result of a Verify (doctored-document) analysis.

    Raw per-signal detail (evidence list, per-family sub-scores, raw regions,
    forensic heatmaps) is available separately via the job's details endpoint.
    """

    detector_version: str
    """Version of the detector that produced the result"""

    overall_score: float
    """Overall doctoring likelihood (0 to 1)"""

    verdict: Literal["AUTHENTIC", "DOCTORED", "LIKELY_DOCTORED", "NO_STRONG_SIGNAL", "SUSPICIOUS"]
    """Overall verdict for the document"""

    composite_scores: Optional[ResultCompositeScores] = None
    """Composite scores, each answering one question about the document"""

    confidence: Optional[float] = None
    """
    Confidence in the verdict (0 to 1): how firmly the detected signals support the
    verdict bucket, independent of the doctoring likelihood itself
    """

    error: Optional[str] = None
    """Error detail when the analysis could not complete"""

    page_count: Optional[int] = None
    """Number of analysed pages (1 for images/docx)"""

    page_dimensions: Optional[List[ResultPageDimension]] = None
    """Rendered pixel size per page, so region bboxes can be scaled onto the page"""

    reasoning: Optional[str] = None
    """Explanation of the verdict"""

    suspect_regions: Optional[List[ResultSuspectRegion]] = None
    """
    Regions that led to the suspected fraud, ranked most-suspect first, each with an
    explanation of what makes it suspect
    """

    synthetic_score: Optional[float] = None
    """
    Likelihood (0 to 1) that the document is wholly generated or fabricated rather
    than a capture of a real document. Null for jobs completed before this score was
    introduced
    """

    tampering_score: Optional[float] = None
    """
    Likelihood (0 to 1) that a real captured document was locally edited — a genuine
    capture with regions altered after the fact. Null for jobs completed before this
    score was introduced
    """


class VerifyGetResponse(BaseModel):
    """Response for a Verify job."""

    id: str
    """Unique identifier"""

    configuration: Configuration
    """Verify configuration used for this job"""

    document_input_type: Literal["file_id", "parse_job_id", "url"]
    """Type of the document input (FILE)"""

    file_input: str
    """ID of the input file"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
    """Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED"""

    user_id: str
    """User who created this job"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    result: Optional[Result] = None
    """Result of a Verify (doctored-document) analysis.

    Raw per-signal detail (evidence list, per-family sub-scores, raw regions,
    forensic heatmaps) is available separately via the job's details endpoint.
    """

    transaction_id: Optional[str] = None
    """Idempotency key"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
