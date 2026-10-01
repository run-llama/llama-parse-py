# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatGetSummaryResponse", "JobMetadata"]


class JobMetadata(BaseModel):
    """Token usage and status from the most recent run.

    Null if the session has not been run yet.
    """

    duration_ms: Optional[float] = None

    error: Optional[str] = None

    export_config_ids: Optional[List[str]] = None

    is_error: Optional[bool] = None

    total_input_tokens: Optional[int] = None

    total_output_tokens: Optional[int] = None

    turns: Optional[int] = None


class ChatGetSummaryResponse(BaseModel):
    """Summary of a chat session, including its title and last run metadata."""

    last_updated_at: str
    """ISO-format timestamp showing when the session was last updated."""

    session_id: str
    """Unique session identifier."""

    shared_access: Literal["query", "read_only"]
    """
    What this chat's share link grants: read_only (transcript only) or query
    (viewers may ask new questions).
    """

    generated_title: Optional[str] = None
    """Auto-generated title derived from the first user message."""

    index_ids: Optional[List[str]] = None
    """Indexes this session is bound to. Null on unbound sessions."""

    job_metadata: Optional[JobMetadata] = None
    """Token usage and status from the most recent run.

    Null if the session has not been run yet.
    """
