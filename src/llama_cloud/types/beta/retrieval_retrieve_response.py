# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel

__all__ = ["RetrievalRetrieveResponse", "Result", "ResultStaticFields", "ResultStaticFieldsAttachment"]


class ResultStaticFieldsAttachment(BaseModel):
    """
    Reference to a file attachment, retrievable via ``GET /api/v1/beta/attachments/{attachment_name}?source_id=...``.
    """

    attachment_name: str
    """Attachment-relative path, e.g. 'screenshots/page_7.jpg'."""

    source_id: str
    """File ID to pass as source_id when fetching the attachment."""

    type: str
    """Attachment kind, e.g. 'screenshot', 'items'."""


class ResultStaticFields(BaseModel):
    """Built-in fields stored for every exported chunk."""

    attachments: Optional[List[ResultStaticFieldsAttachment]] = None
    """Attachments associated with the chunk"""

    chunk_end_char: Optional[int] = None
    """End character offset of the chunk."""

    chunk_index: Optional[int] = None
    """Index of the chunk within the file."""

    chunk_start_char: Optional[int] = None
    """Start character offset of the chunk."""

    chunk_token_count: Optional[int] = None
    """Token count of the chunk."""

    page_range_end: Optional[int] = None
    """Last page number covered by this chunk."""

    page_range_start: Optional[int] = None
    """First page number covered by this chunk."""

    parsed_directory_file_id: Optional[str] = None
    """ID of the parsed file."""


class Result(BaseModel):
    """A single retrieval result."""

    content: str
    """Text content of the retrieved chunk."""

    metadata: Optional[Dict[str, Union[str, float, bool, List[str], None]]] = None
    """User-defined metadata associated with the chunk."""

    rerank_score: Optional[float] = None
    """Relevance score from the reranker, if reranking was applied."""

    score: Optional[float] = None
    """Hybrid search relevance score."""

    static_fields: Optional[ResultStaticFields] = None
    """Built-in fields stored for every exported chunk."""


class RetrievalRetrieveResponse(BaseModel):
    """Response containing retrieval results."""

    results: List[Result]
    """Ordered list of retrieved chunks."""
