# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .data_sink import DataSink
from .pipeline_type import PipelineType
from .sparse_model_config import SparseModelConfig
from .auto_transform_config import AutoTransformConfig
from .llama_parse_parameters import LlamaParseParameters
from .cohere_embedding_config import CohereEmbeddingConfig
from .gemini_embedding_config import GeminiEmbeddingConfig
from .openai_embedding_config import OpenAIEmbeddingConfig
from .bedrock_embedding_config import BedrockEmbeddingConfig
from .pipeline_metadata_config import PipelineMetadataConfig
from .vertex_ai_embedding_config import VertexAIEmbeddingConfig
from .azure_openai_embedding_config import AzureOpenAIEmbeddingConfig
from .advanced_mode_transform_config import AdvancedModeTransformConfig
from .hugging_face_inference_api_embedding_config import HuggingFaceInferenceAPIEmbeddingConfig

__all__ = [
    "Pipeline",
    "EmbeddingConfig",
    "EmbeddingConfigManagedOpenAIEmbeddingConfig",
    "EmbeddingConfigManagedOpenAIEmbeddingConfigComponent",
    "ConfigHash",
    "EmbeddingModelConfig",
    "EmbeddingModelConfigEmbeddingConfig",
    "TransformConfig",
]


class EmbeddingConfigManagedOpenAIEmbeddingConfigComponent(BaseModel):
    """Configuration for the Managed OpenAI embedding model."""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    api_model_name: Optional[Literal["openai-text-embedding-3-small"]] = FieldInfo(alias="model_name", default=None)
    """The name of the OpenAI embedding model."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""


class EmbeddingConfigManagedOpenAIEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigManagedOpenAIEmbeddingConfigComponent] = None
    """Configuration for the Managed OpenAI embedding model."""

    type: Optional[Literal["MANAGED_OPENAI_EMBEDDING"]] = None
    """Type of the embedding model."""


EmbeddingConfig: TypeAlias = Annotated[
    Union[
        AzureOpenAIEmbeddingConfig,
        BedrockEmbeddingConfig,
        CohereEmbeddingConfig,
        GeminiEmbeddingConfig,
        HuggingFaceInferenceAPIEmbeddingConfig,
        EmbeddingConfigManagedOpenAIEmbeddingConfig,
        OpenAIEmbeddingConfig,
        VertexAIEmbeddingConfig,
    ],
    PropertyInfo(discriminator="type"),
]


class ConfigHash(BaseModel):
    """Hashes for the configuration of a pipeline."""

    embedding_config_hash: Optional[str] = None
    """Hash of the embedding config."""

    parsing_config_hash: Optional[str] = None
    """Hash of the llama parse parameters."""

    transform_config_hash: Optional[str] = None
    """Hash of the transform config."""


EmbeddingModelConfigEmbeddingConfig: TypeAlias = Annotated[
    Union[
        AzureOpenAIEmbeddingConfig,
        BedrockEmbeddingConfig,
        CohereEmbeddingConfig,
        GeminiEmbeddingConfig,
        HuggingFaceInferenceAPIEmbeddingConfig,
        OpenAIEmbeddingConfig,
        VertexAIEmbeddingConfig,
    ],
    PropertyInfo(discriminator="type"),
]


class EmbeddingModelConfig(BaseModel):
    """Schema for an embedding model config."""

    id: str
    """Unique identifier"""

    embedding_config: EmbeddingModelConfigEmbeddingConfig
    """The embedding configuration for the embedding model config."""

    name: str
    """The name of the embedding model config."""

    project_id: str

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""


TransformConfig: TypeAlias = Union[AutoTransformConfig, AdvancedModeTransformConfig]


class Pipeline(BaseModel):
    """Schema for a pipeline."""

    id: str
    """Unique identifier"""

    embedding_config: EmbeddingConfig

    name: str

    project_id: str

    config_hash: Optional[ConfigHash] = None
    """Hashes for the configuration of a pipeline."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    data_sink: Optional[DataSink] = None
    """Schema for a data sink."""

    embedding_model_config: Optional[EmbeddingModelConfig] = None
    """Schema for an embedding model config."""

    embedding_model_config_id: Optional[str] = None
    """The ID of the EmbeddingModelConfig this pipeline is using."""

    llama_parse_parameters: Optional[LlamaParseParameters] = None
    """
    Settings that can be configured for how to use LlamaParse to parse files within
    a LlamaCloud pipeline.
    """

    managed_pipeline_id: Optional[str] = None
    """The ID of the ManagedPipeline this playground pipeline is linked to."""

    metadata_config: Optional[PipelineMetadataConfig] = None
    """Metadata configuration for the pipeline."""

    pipeline_type: Optional[PipelineType] = None
    """Type of pipeline. Either PLAYGROUND or MANAGED."""

    preset_retrieval_parameters: Optional["PresetRetrievalParams"] = None
    """Preset retrieval parameters for the pipeline."""

    sparse_model_config: Optional[SparseModelConfig] = None
    """Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for sparse retrieval
    in managed data sinks.
    """

    status: Optional[Literal["CREATED", "DELETING"]] = None
    """Status of the pipeline."""

    transform_config: Optional[TransformConfig] = None
    """Configuration for the transformation."""

    updated_at: Optional[datetime] = None
    """Update datetime"""


from .preset_retrieval_params import PresetRetrievalParams
