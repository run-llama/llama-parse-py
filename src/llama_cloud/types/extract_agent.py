# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractAgent", "Config"]


class Config(BaseModel):
    """The configuration parameters for the extraction agent."""

    chunk_mode: Optional[Literal["PAGE", "SECTION"]] = None
    """The mode to use for chunking the document."""

    citation_bbox: Optional[bool] = None
    """Whether to fetch citation bounding boxes for the extraction.

    Only available in PREMIUM mode. Deprecated: this is now synonymous with
    cite_sources.
    """

    cite_sources: Optional[bool] = None
    """Whether to cite sources for the extraction."""

    confidence_scores: Optional[bool] = None
    """Whether to fetch confidence scores for the extraction."""

    extract_model: Union[
        Literal[
            "gemini-2.0-flash",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-2.5-pro",
            "openai-gpt-4-1",
            "openai-gpt-4-1-mini",
            "openai-gpt-4-1-nano",
            "openai-gpt-4o",
            "openai-gpt-4o-mini",
            "openai-gpt-5",
            "openai-gpt-5-mini",
        ],
        str,
        None,
    ] = None
    """The extract model to use for data extraction.

    If not provided, uses the default for the extraction mode.
    """

    extraction_mode: Optional[Literal["BALANCED", "FAST", "MULTIMODAL", "PREMIUM"]] = None
    """The extraction mode specified (FAST, BALANCED, MULTIMODAL, PREMIUM)."""

    extraction_target: Optional[Literal["PER_DOC", "PER_PAGE", "PER_TABLE_ROW"]] = None
    """The extraction target specified."""

    high_resolution_mode: Optional[bool] = None
    """Whether to use high resolution mode for the extraction."""

    invalidate_cache: Optional[bool] = None
    """Whether to invalidate the cache for the extraction."""

    multimodal_fast_mode: Optional[bool] = None
    """DEPRECATED: Whether to use fast mode for multimodal extraction."""

    num_pages_context: Optional[int] = None
    """Number of pages to pass as context on long document extraction."""

    page_range: Optional[str] = None
    """
    Comma-separated list of page numbers or ranges to extract from (1-based, e.g.,
    '1,3,5-7,9' or '1-3,8-10').
    """

    parse_model: Optional[
        Literal[
            "anthropic-haiku-3.5",
            "anthropic-haiku-4.5",
            "anthropic-sonnet-3.5",
            "anthropic-sonnet-3.5-v2",
            "anthropic-sonnet-3.7",
            "anthropic-sonnet-4.0",
            "anthropic-sonnet-4.5",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-2.5-pro",
            "gemini-3.0-pro",
            "gemini-3.1-pro",
            "openai-gpt-4-1",
            "openai-gpt-4-1-mini",
            "openai-gpt-4-1-nano",
            "openai-gpt-4o",
            "openai-gpt-4o-mini",
            "openai-gpt-5",
            "openai-gpt-5-mini",
            "openai-gpt-5-nano",
            "openai-text-embedding-3-large",
            "openai-text-embedding-3-small",
            "openai-whisper-1",
        ]
    ] = None
    """Public model names."""

    priority: Optional[Literal["critical", "high", "low", "medium"]] = None
    """The priority for the request.

    This field may be ignored or overwritten depending on the organization tier.
    """

    system_prompt: Optional[str] = None
    """The system prompt to use for the extraction."""

    use_reasoning: Optional[bool] = None
    """Whether to use reasoning for the extraction."""


class ExtractAgent(BaseModel):
    """Schema and configuration for an extraction agent."""

    id: str
    """The id of the extraction agent."""

    config: Config
    """The configuration parameters for the extraction agent."""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """The schema of the data."""

    name: str
    """The name of the extraction agent."""

    project_id: str
    """The ID of the project that the extraction agent belongs to."""

    created_at: Optional[datetime] = None
    """The creation time of the extraction agent."""

    custom_configuration: Optional[Literal["default"]] = None
    """Custom configuration type for the extraction agent.

    Currently supports 'default'.
    """

    updated_at: Optional[datetime] = None
    """The last update time of the extraction agent."""
