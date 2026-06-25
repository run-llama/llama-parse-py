# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .pipeline_type import PipelineType
from .data_sink_create_param import DataSinkCreateParam
from .sparse_model_config_param import SparseModelConfigParam
from .auto_transform_config_param import AutoTransformConfigParam
from .llama_parse_parameters_param import LlamaParseParametersParam
from .cohere_embedding_config_param import CohereEmbeddingConfigParam
from .gemini_embedding_config_param import GeminiEmbeddingConfigParam
from .openai_embedding_config_param import OpenAIEmbeddingConfigParam
from .bedrock_embedding_config_param import BedrockEmbeddingConfigParam
from .pipeline_metadata_config_param import PipelineMetadataConfigParam
from .vertex_ai_embedding_config_param import VertexAIEmbeddingConfigParam
from .azure_openai_embedding_config_param import AzureOpenAIEmbeddingConfigParam
from .advanced_mode_transform_config_param import AdvancedModeTransformConfigParam
from .hugging_face_inference_api_embedding_config_param import HuggingFaceInferenceAPIEmbeddingConfigParam

__all__ = ["PipelineCreateParams", "EmbeddingConfig", "TransformConfig"]


class PipelineCreateParams(TypedDict, total=False):
    name: Required[str]

    organization_id: Optional[str]

    project_id: Optional[str]

    data_sink: Optional[DataSinkCreateParam]
    """Schema for creating a data sink."""

    data_sink_id: Optional[str]
    """Data sink ID.

    When provided instead of data_sink, the data sink will be looked up by ID.
    """

    embedding_config: Optional[EmbeddingConfig]

    embedding_model_config_id: Optional[str]
    """Embedding model config ID.

    When provided instead of embedding_config, the embedding model config will be
    looked up by ID.
    """

    llama_parse_parameters: LlamaParseParametersParam
    """
    Settings that can be configured for how to use LlamaParse to parse files within
    a LlamaCloud pipeline.
    """

    managed_pipeline_id: Optional[str]
    """The ID of the ManagedPipeline this playground pipeline is linked to."""

    metadata_config: Optional[PipelineMetadataConfigParam]
    """Metadata configuration for the pipeline."""

    pipeline_type: PipelineType
    """Type of pipeline. Either PLAYGROUND or MANAGED."""

    preset_retrieval_parameters: "PresetRetrievalParamsParam"
    """Preset retrieval parameters for the pipeline."""

    sparse_model_config: Optional[SparseModelConfigParam]
    """Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for sparse retrieval
    in managed data sinks.
    """

    status: Optional[str]
    """Status of the pipeline deployment."""

    transform_config: Optional[TransformConfig]
    """Configuration for the transformation."""


EmbeddingConfig: TypeAlias = Union[
    AzureOpenAIEmbeddingConfigParam,
    BedrockEmbeddingConfigParam,
    CohereEmbeddingConfigParam,
    GeminiEmbeddingConfigParam,
    HuggingFaceInferenceAPIEmbeddingConfigParam,
    OpenAIEmbeddingConfigParam,
    VertexAIEmbeddingConfigParam,
]

TransformConfig: TypeAlias = Union[AutoTransformConfigParam, AdvancedModeTransformConfigParam]

from .preset_retrieval_params_param import PresetRetrievalParamsParam
