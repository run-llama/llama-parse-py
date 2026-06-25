# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VertexTextEmbeddingParam"]


class VertexTextEmbeddingParam(TypedDict, total=False):
    client_email: Required[Optional[str]]
    """The client email for the VertexAI credentials."""

    location: Required[str]
    """The default location to use when making API calls."""

    private_key: Required[Optional[str]]
    """The private key for the VertexAI credentials."""

    private_key_id: Required[Optional[str]]
    """The private key ID for the VertexAI credentials."""

    project: Required[str]
    """The default GCP project to use when making Vertex API calls."""

    token_uri: Required[Optional[str]]
    """The token URI for the VertexAI credentials."""

    additional_kwargs: Dict[str, object]
    """Additional kwargs for the Vertex."""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    embed_mode: Literal["classification", "clustering", "default", "retrieval", "similarity"]
    """The embedding mode to use."""

    model_name: str
    """The modelId of the VertexAI model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""
