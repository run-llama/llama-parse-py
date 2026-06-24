# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VertexTextEmbedding"]


class VertexTextEmbedding(BaseModel):
    client_email: Optional[str] = None
    """The client email for the VertexAI credentials."""

    location: str
    """The default location to use when making API calls."""

    private_key: Optional[str] = None
    """The private key for the VertexAI credentials."""

    private_key_id: Optional[str] = None
    """The private key ID for the VertexAI credentials."""

    project: str
    """The default GCP project to use when making Vertex API calls."""

    token_uri: Optional[str] = None
    """The token URI for the VertexAI credentials."""

    additional_kwargs: Optional[Dict[str, object]] = None
    """Additional kwargs for the Vertex."""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    embed_mode: Optional[Literal["classification", "clustering", "default", "retrieval", "similarity"]] = None
    """The embedding mode to use."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the VertexAI model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""
