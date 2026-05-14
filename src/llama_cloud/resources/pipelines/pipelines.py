# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from .sync import (
    SyncResource,
    AsyncSyncResource,
    SyncResourceWithRawResponse,
    AsyncSyncResourceWithRawResponse,
    SyncResourceWithStreamingResponse,
    AsyncSyncResourceWithStreamingResponse,
)
from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ...types import (
    PipelineType,
    RetrievalMode,
    pipeline_list_params,
    pipeline_create_params,
    pipeline_update_params,
    pipeline_upsert_params,
    pipeline_retrieve_params,
    pipeline_get_status_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .data_sources import (
    DataSourcesResource,
    AsyncDataSourcesResource,
    DataSourcesResourceWithRawResponse,
    AsyncDataSourcesResourceWithRawResponse,
    DataSourcesResourceWithStreamingResponse,
    AsyncDataSourcesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.pipeline import Pipeline
from ...types.pipeline_type import PipelineType
from ...types.retrieval_mode import RetrievalMode
from ...types.data_sink_create_param import DataSinkCreateParam
from ...types.metadata_filters_param import MetadataFiltersParam
from ...types.pipeline_list_response import PipelineListResponse
from ...types.sparse_model_config_param import SparseModelConfigParam
from ...types.pipeline_retrieve_response import PipelineRetrieveResponse
from ...types.llama_parse_parameters_param import LlamaParseParametersParam
from ...types.preset_retrieval_params_param import PresetRetrievalParamsParam
from ...types.pipeline_metadata_config_param import PipelineMetadataConfigParam
from ...types.managed_ingestion_status_response import ManagedIngestionStatusResponse

__all__ = ["PipelinesResource", "AsyncPipelinesResource"]


class PipelinesResource(SyncAPIResource):
    @cached_property
    def sync(self) -> SyncResource:
        return SyncResource(self._client)

    @cached_property
    def data_sources(self) -> DataSourcesResource:
        return DataSourcesResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return PipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return PipelinesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_sink: Optional[DataSinkCreateParam] | Omit = omit,
        data_sink_id: Optional[str] | Omit = omit,
        embedding_config: Optional[pipeline_create_params.EmbeddingConfig] | Omit = omit,
        embedding_model_config_id: Optional[str] | Omit = omit,
        llama_parse_parameters: LlamaParseParametersParam | Omit = omit,
        managed_pipeline_id: Optional[str] | Omit = omit,
        metadata_config: Optional[PipelineMetadataConfigParam] | Omit = omit,
        pipeline_type: PipelineType | Omit = omit,
        preset_retrieval_parameters: PresetRetrievalParamsParam | Omit = omit,
        sparse_model_config: Optional[SparseModelConfigParam] | Omit = omit,
        status: Optional[str] | Omit = omit,
        transform_config: Optional[pipeline_create_params.TransformConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Create a new managed ingestion pipeline.

        A pipeline connects data sources to a vector store for RAG. After creation, call
        `POST /pipelines/{id}/sync` to start ingesting documents.

        Args:
          data_sink: Schema for creating a data sink.

          data_sink_id: Data sink ID. When provided instead of data_sink, the data sink will be looked
              up by ID.

          embedding_model_config_id: Embedding model config ID. When provided instead of embedding_config, the
              embedding model config will be looked up by ID.

          llama_parse_parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          managed_pipeline_id: The ID of the ManagedPipeline this playground pipeline is linked to.

          metadata_config: Metadata configuration for the pipeline.

          pipeline_type: Type of pipeline. Either PLAYGROUND or MANAGED.

          preset_retrieval_parameters: Preset retrieval parameters for the pipeline.

          sparse_model_config: Configuration for sparse embedding models used in hybrid search.

              This allows users to choose between Splade and BM25 models for sparse retrieval
              in managed data sinks.

          status: Status of the pipeline deployment.

          transform_config: Configuration for the transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/pipelines",
            body=maybe_transform(
                {
                    "name": name,
                    "data_sink": data_sink,
                    "data_sink_id": data_sink_id,
                    "embedding_config": embedding_config,
                    "embedding_model_config_id": embedding_model_config_id,
                    "llama_parse_parameters": llama_parse_parameters,
                    "managed_pipeline_id": managed_pipeline_id,
                    "metadata_config": metadata_config,
                    "pipeline_type": pipeline_type,
                    "preset_retrieval_parameters": preset_retrieval_parameters,
                    "sparse_model_config": sparse_model_config,
                    "status": status,
                    "transform_config": transform_config,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    pipeline_create_params.PipelineCreateParams,
                ),
            ),
            cast_to=Pipeline,
        )

    def retrieve(
        self,
        pipeline_id: str,
        *,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        alpha: Optional[float] | Omit = omit,
        class_name: str | Omit = omit,
        dense_similarity_cutoff: Optional[float] | Omit = omit,
        dense_similarity_top_k: Optional[int] | Omit = omit,
        enable_reranking: Optional[bool] | Omit = omit,
        files_top_k: Optional[int] | Omit = omit,
        rerank_top_n: Optional[int] | Omit = omit,
        retrieval_mode: RetrievalMode | Omit = omit,
        retrieve_image_nodes: bool | Omit = omit,
        retrieve_page_figure_nodes: bool | Omit = omit,
        retrieve_page_screenshot_nodes: bool | Omit = omit,
        search_filters: Optional[MetadataFiltersParam] | Omit = omit,
        search_filters_inference_schema: Optional[
            Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]
        ]
        | Omit = omit,
        sparse_similarity_top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineRetrieveResponse:
        """
        Run a retrieval query against a managed pipeline.

        Searches the pipeline's vector store using the provided query and retrieval
        parameters. Supports dense, sparse, and hybrid search modes with configurable
        top-k and reranking.

        Args:
          query: The query to retrieve against.

          alpha: Alpha value for hybrid retrieval to determine the weights between dense and
              sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

          dense_similarity_cutoff: Minimum similarity score wrt query for retrieval

          dense_similarity_top_k: Number of nodes for dense retrieval.

          enable_reranking: Enable reranking for retrieval

          files_top_k: Number of files to retrieve (only for retrieval mode files_via_metadata and
              files_via_content).

          rerank_top_n: Number of reranked nodes for returning.

          retrieval_mode: The retrieval mode for the query.

          retrieve_image_nodes: Whether to retrieve image nodes.

          retrieve_page_figure_nodes: Whether to retrieve page figure nodes.

          retrieve_page_screenshot_nodes: Whether to retrieve page screenshot nodes.

          search_filters: Metadata filters for vector stores.

          search_filters_inference_schema: JSON Schema that will be used to infer search_filters. Omit or leave as null to
              skip inference.

          sparse_similarity_top_k: Number of nodes for sparse retrieval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._post(
            path_template("/api/v1/pipelines/{pipeline_id}/retrieve", pipeline_id=pipeline_id),
            body=maybe_transform(
                {
                    "query": query,
                    "alpha": alpha,
                    "class_name": class_name,
                    "dense_similarity_cutoff": dense_similarity_cutoff,
                    "dense_similarity_top_k": dense_similarity_top_k,
                    "enable_reranking": enable_reranking,
                    "files_top_k": files_top_k,
                    "rerank_top_n": rerank_top_n,
                    "retrieval_mode": retrieval_mode,
                    "retrieve_image_nodes": retrieve_image_nodes,
                    "retrieve_page_figure_nodes": retrieve_page_figure_nodes,
                    "retrieve_page_screenshot_nodes": retrieve_page_screenshot_nodes,
                    "search_filters": search_filters,
                    "search_filters_inference_schema": search_filters_inference_schema,
                    "sparse_similarity_top_k": sparse_similarity_top_k,
                },
                pipeline_retrieve_params.PipelineRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    pipeline_retrieve_params.PipelineRetrieveParams,
                ),
            ),
            cast_to=PipelineRetrieveResponse,
        )

    def update(
        self,
        pipeline_id: str,
        *,
        data_sink: Optional[DataSinkCreateParam] | Omit = omit,
        data_sink_id: Optional[str] | Omit = omit,
        embedding_config: Optional[pipeline_update_params.EmbeddingConfig] | Omit = omit,
        embedding_model_config_id: Optional[str] | Omit = omit,
        llama_parse_parameters: Optional[LlamaParseParametersParam] | Omit = omit,
        managed_pipeline_id: Optional[str] | Omit = omit,
        metadata_config: Optional[PipelineMetadataConfigParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preset_retrieval_parameters: Optional[PresetRetrievalParamsParam] | Omit = omit,
        sparse_model_config: Optional[SparseModelConfigParam] | Omit = omit,
        status: Optional[str] | Omit = omit,
        transform_config: Optional[pipeline_update_params.TransformConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Update an existing pipeline's configuration.

        Args:
          data_sink: Schema for creating a data sink.

          data_sink_id: Data sink ID. When provided instead of data_sink, the data sink will be looked
              up by ID.

          embedding_model_config_id: Embedding model config ID. When provided instead of embedding_config, the
              embedding model config will be looked up by ID.

          llama_parse_parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          managed_pipeline_id: The ID of the ManagedPipeline this playground pipeline is linked to.

          metadata_config: Metadata configuration for the pipeline.

          preset_retrieval_parameters: Schema for the search params for an retrieval execution that can be preset for a
              pipeline.

          sparse_model_config: Configuration for sparse embedding models used in hybrid search.

              This allows users to choose between Splade and BM25 models for sparse retrieval
              in managed data sinks.

          status: Status of the pipeline deployment.

          transform_config: Configuration for the transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._put(
            path_template("/api/v1/pipelines/{pipeline_id}", pipeline_id=pipeline_id),
            body=maybe_transform(
                {
                    "data_sink": data_sink,
                    "data_sink_id": data_sink_id,
                    "embedding_config": embedding_config,
                    "embedding_model_config_id": embedding_model_config_id,
                    "llama_parse_parameters": llama_parse_parameters,
                    "managed_pipeline_id": managed_pipeline_id,
                    "metadata_config": metadata_config,
                    "name": name,
                    "preset_retrieval_parameters": preset_retrieval_parameters,
                    "sparse_model_config": sparse_model_config,
                    "status": status,
                    "transform_config": transform_config,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        pipeline_name: Optional[str] | Omit = omit,
        pipeline_type: Optional[PipelineType] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        project_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineListResponse:
        """
        Search for pipelines by name, type, or project.

        Args:
          pipeline_type: Enum for representing the type of a pipeline

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/pipelines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "pipeline_name": pipeline_name,
                        "pipeline_type": pipeline_type,
                        "project_id": project_id,
                        "project_name": project_name,
                    },
                    pipeline_list_params.PipelineListParams,
                ),
            ),
            cast_to=PipelineListResponse,
        )

    def delete(
        self,
        pipeline_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a pipeline and all associated resources.

        Removes pipeline files, data sources, and vector store data. This operation is
        irreversible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/pipelines/{pipeline_id}", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        pipeline_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Get a pipeline by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            path_template("/api/v1/pipelines/{pipeline_id}", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    def get_status(
        self,
        pipeline_id: str,
        *,
        full_details: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedIngestionStatusResponse:
        """
        Get the ingestion status of a managed pipeline.

        Returns document counts, sync progress, and the last effective timestamp. Only
        available for managed pipelines.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            path_template("/api/v1/pipelines/{pipeline_id}/status", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"full_details": full_details}, pipeline_get_status_params.PipelineGetStatusParams
                ),
            ),
            cast_to=ManagedIngestionStatusResponse,
        )

    def upsert(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_sink: Optional[DataSinkCreateParam] | Omit = omit,
        data_sink_id: Optional[str] | Omit = omit,
        embedding_config: Optional[pipeline_upsert_params.EmbeddingConfig] | Omit = omit,
        embedding_model_config_id: Optional[str] | Omit = omit,
        llama_parse_parameters: LlamaParseParametersParam | Omit = omit,
        managed_pipeline_id: Optional[str] | Omit = omit,
        metadata_config: Optional[PipelineMetadataConfigParam] | Omit = omit,
        pipeline_type: PipelineType | Omit = omit,
        preset_retrieval_parameters: PresetRetrievalParamsParam | Omit = omit,
        sparse_model_config: Optional[SparseModelConfigParam] | Omit = omit,
        status: Optional[str] | Omit = omit,
        transform_config: Optional[pipeline_upsert_params.TransformConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Upsert a pipeline.

        Updates the pipeline if one with the same name and project already exists,
        otherwise creates a new one.

        Args:
          data_sink: Schema for creating a data sink.

          data_sink_id: Data sink ID. When provided instead of data_sink, the data sink will be looked
              up by ID.

          embedding_model_config_id: Embedding model config ID. When provided instead of embedding_config, the
              embedding model config will be looked up by ID.

          llama_parse_parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          managed_pipeline_id: The ID of the ManagedPipeline this playground pipeline is linked to.

          metadata_config: Metadata configuration for the pipeline.

          pipeline_type: Type of pipeline. Either PLAYGROUND or MANAGED.

          preset_retrieval_parameters: Preset retrieval parameters for the pipeline.

          sparse_model_config: Configuration for sparse embedding models used in hybrid search.

              This allows users to choose between Splade and BM25 models for sparse retrieval
              in managed data sinks.

          status: Status of the pipeline deployment.

          transform_config: Configuration for the transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1/pipelines",
            body=maybe_transform(
                {
                    "name": name,
                    "data_sink": data_sink,
                    "data_sink_id": data_sink_id,
                    "embedding_config": embedding_config,
                    "embedding_model_config_id": embedding_model_config_id,
                    "llama_parse_parameters": llama_parse_parameters,
                    "managed_pipeline_id": managed_pipeline_id,
                    "metadata_config": metadata_config,
                    "pipeline_type": pipeline_type,
                    "preset_retrieval_parameters": preset_retrieval_parameters,
                    "sparse_model_config": sparse_model_config,
                    "status": status,
                    "transform_config": transform_config,
                },
                pipeline_upsert_params.PipelineUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    pipeline_upsert_params.PipelineUpsertParams,
                ),
            ),
            cast_to=Pipeline,
        )


class AsyncPipelinesResource(AsyncAPIResource):
    @cached_property
    def sync(self) -> AsyncSyncResource:
        return AsyncSyncResource(self._client)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResource:
        return AsyncDataSourcesResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncPipelinesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_sink: Optional[DataSinkCreateParam] | Omit = omit,
        data_sink_id: Optional[str] | Omit = omit,
        embedding_config: Optional[pipeline_create_params.EmbeddingConfig] | Omit = omit,
        embedding_model_config_id: Optional[str] | Omit = omit,
        llama_parse_parameters: LlamaParseParametersParam | Omit = omit,
        managed_pipeline_id: Optional[str] | Omit = omit,
        metadata_config: Optional[PipelineMetadataConfigParam] | Omit = omit,
        pipeline_type: PipelineType | Omit = omit,
        preset_retrieval_parameters: PresetRetrievalParamsParam | Omit = omit,
        sparse_model_config: Optional[SparseModelConfigParam] | Omit = omit,
        status: Optional[str] | Omit = omit,
        transform_config: Optional[pipeline_create_params.TransformConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Create a new managed ingestion pipeline.

        A pipeline connects data sources to a vector store for RAG. After creation, call
        `POST /pipelines/{id}/sync` to start ingesting documents.

        Args:
          data_sink: Schema for creating a data sink.

          data_sink_id: Data sink ID. When provided instead of data_sink, the data sink will be looked
              up by ID.

          embedding_model_config_id: Embedding model config ID. When provided instead of embedding_config, the
              embedding model config will be looked up by ID.

          llama_parse_parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          managed_pipeline_id: The ID of the ManagedPipeline this playground pipeline is linked to.

          metadata_config: Metadata configuration for the pipeline.

          pipeline_type: Type of pipeline. Either PLAYGROUND or MANAGED.

          preset_retrieval_parameters: Preset retrieval parameters for the pipeline.

          sparse_model_config: Configuration for sparse embedding models used in hybrid search.

              This allows users to choose between Splade and BM25 models for sparse retrieval
              in managed data sinks.

          status: Status of the pipeline deployment.

          transform_config: Configuration for the transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/pipelines",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "data_sink": data_sink,
                    "data_sink_id": data_sink_id,
                    "embedding_config": embedding_config,
                    "embedding_model_config_id": embedding_model_config_id,
                    "llama_parse_parameters": llama_parse_parameters,
                    "managed_pipeline_id": managed_pipeline_id,
                    "metadata_config": metadata_config,
                    "pipeline_type": pipeline_type,
                    "preset_retrieval_parameters": preset_retrieval_parameters,
                    "sparse_model_config": sparse_model_config,
                    "status": status,
                    "transform_config": transform_config,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    pipeline_create_params.PipelineCreateParams,
                ),
            ),
            cast_to=Pipeline,
        )

    async def retrieve(
        self,
        pipeline_id: str,
        *,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        alpha: Optional[float] | Omit = omit,
        class_name: str | Omit = omit,
        dense_similarity_cutoff: Optional[float] | Omit = omit,
        dense_similarity_top_k: Optional[int] | Omit = omit,
        enable_reranking: Optional[bool] | Omit = omit,
        files_top_k: Optional[int] | Omit = omit,
        rerank_top_n: Optional[int] | Omit = omit,
        retrieval_mode: RetrievalMode | Omit = omit,
        retrieve_image_nodes: bool | Omit = omit,
        retrieve_page_figure_nodes: bool | Omit = omit,
        retrieve_page_screenshot_nodes: bool | Omit = omit,
        search_filters: Optional[MetadataFiltersParam] | Omit = omit,
        search_filters_inference_schema: Optional[
            Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]
        ]
        | Omit = omit,
        sparse_similarity_top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineRetrieveResponse:
        """
        Run a retrieval query against a managed pipeline.

        Searches the pipeline's vector store using the provided query and retrieval
        parameters. Supports dense, sparse, and hybrid search modes with configurable
        top-k and reranking.

        Args:
          query: The query to retrieve against.

          alpha: Alpha value for hybrid retrieval to determine the weights between dense and
              sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

          dense_similarity_cutoff: Minimum similarity score wrt query for retrieval

          dense_similarity_top_k: Number of nodes for dense retrieval.

          enable_reranking: Enable reranking for retrieval

          files_top_k: Number of files to retrieve (only for retrieval mode files_via_metadata and
              files_via_content).

          rerank_top_n: Number of reranked nodes for returning.

          retrieval_mode: The retrieval mode for the query.

          retrieve_image_nodes: Whether to retrieve image nodes.

          retrieve_page_figure_nodes: Whether to retrieve page figure nodes.

          retrieve_page_screenshot_nodes: Whether to retrieve page screenshot nodes.

          search_filters: Metadata filters for vector stores.

          search_filters_inference_schema: JSON Schema that will be used to infer search_filters. Omit or leave as null to
              skip inference.

          sparse_similarity_top_k: Number of nodes for sparse retrieval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._post(
            path_template("/api/v1/pipelines/{pipeline_id}/retrieve", pipeline_id=pipeline_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "alpha": alpha,
                    "class_name": class_name,
                    "dense_similarity_cutoff": dense_similarity_cutoff,
                    "dense_similarity_top_k": dense_similarity_top_k,
                    "enable_reranking": enable_reranking,
                    "files_top_k": files_top_k,
                    "rerank_top_n": rerank_top_n,
                    "retrieval_mode": retrieval_mode,
                    "retrieve_image_nodes": retrieve_image_nodes,
                    "retrieve_page_figure_nodes": retrieve_page_figure_nodes,
                    "retrieve_page_screenshot_nodes": retrieve_page_screenshot_nodes,
                    "search_filters": search_filters,
                    "search_filters_inference_schema": search_filters_inference_schema,
                    "sparse_similarity_top_k": sparse_similarity_top_k,
                },
                pipeline_retrieve_params.PipelineRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    pipeline_retrieve_params.PipelineRetrieveParams,
                ),
            ),
            cast_to=PipelineRetrieveResponse,
        )

    async def update(
        self,
        pipeline_id: str,
        *,
        data_sink: Optional[DataSinkCreateParam] | Omit = omit,
        data_sink_id: Optional[str] | Omit = omit,
        embedding_config: Optional[pipeline_update_params.EmbeddingConfig] | Omit = omit,
        embedding_model_config_id: Optional[str] | Omit = omit,
        llama_parse_parameters: Optional[LlamaParseParametersParam] | Omit = omit,
        managed_pipeline_id: Optional[str] | Omit = omit,
        metadata_config: Optional[PipelineMetadataConfigParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preset_retrieval_parameters: Optional[PresetRetrievalParamsParam] | Omit = omit,
        sparse_model_config: Optional[SparseModelConfigParam] | Omit = omit,
        status: Optional[str] | Omit = omit,
        transform_config: Optional[pipeline_update_params.TransformConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Update an existing pipeline's configuration.

        Args:
          data_sink: Schema for creating a data sink.

          data_sink_id: Data sink ID. When provided instead of data_sink, the data sink will be looked
              up by ID.

          embedding_model_config_id: Embedding model config ID. When provided instead of embedding_config, the
              embedding model config will be looked up by ID.

          llama_parse_parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          managed_pipeline_id: The ID of the ManagedPipeline this playground pipeline is linked to.

          metadata_config: Metadata configuration for the pipeline.

          preset_retrieval_parameters: Schema for the search params for an retrieval execution that can be preset for a
              pipeline.

          sparse_model_config: Configuration for sparse embedding models used in hybrid search.

              This allows users to choose between Splade and BM25 models for sparse retrieval
              in managed data sinks.

          status: Status of the pipeline deployment.

          transform_config: Configuration for the transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._put(
            path_template("/api/v1/pipelines/{pipeline_id}", pipeline_id=pipeline_id),
            body=await async_maybe_transform(
                {
                    "data_sink": data_sink,
                    "data_sink_id": data_sink_id,
                    "embedding_config": embedding_config,
                    "embedding_model_config_id": embedding_model_config_id,
                    "llama_parse_parameters": llama_parse_parameters,
                    "managed_pipeline_id": managed_pipeline_id,
                    "metadata_config": metadata_config,
                    "name": name,
                    "preset_retrieval_parameters": preset_retrieval_parameters,
                    "sparse_model_config": sparse_model_config,
                    "status": status,
                    "transform_config": transform_config,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    async def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        pipeline_name: Optional[str] | Omit = omit,
        pipeline_type: Optional[PipelineType] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        project_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineListResponse:
        """
        Search for pipelines by name, type, or project.

        Args:
          pipeline_type: Enum for representing the type of a pipeline

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/pipelines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "pipeline_name": pipeline_name,
                        "pipeline_type": pipeline_type,
                        "project_id": project_id,
                        "project_name": project_name,
                    },
                    pipeline_list_params.PipelineListParams,
                ),
            ),
            cast_to=PipelineListResponse,
        )

    async def delete(
        self,
        pipeline_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a pipeline and all associated resources.

        Removes pipeline files, data sources, and vector store data. This operation is
        irreversible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/pipelines/{pipeline_id}", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        pipeline_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Get a pipeline by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            path_template("/api/v1/pipelines/{pipeline_id}", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    async def get_status(
        self,
        pipeline_id: str,
        *,
        full_details: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedIngestionStatusResponse:
        """
        Get the ingestion status of a managed pipeline.

        Returns document counts, sync progress, and the last effective timestamp. Only
        available for managed pipelines.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            path_template("/api/v1/pipelines/{pipeline_id}/status", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"full_details": full_details}, pipeline_get_status_params.PipelineGetStatusParams
                ),
            ),
            cast_to=ManagedIngestionStatusResponse,
        )

    async def upsert(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_sink: Optional[DataSinkCreateParam] | Omit = omit,
        data_sink_id: Optional[str] | Omit = omit,
        embedding_config: Optional[pipeline_upsert_params.EmbeddingConfig] | Omit = omit,
        embedding_model_config_id: Optional[str] | Omit = omit,
        llama_parse_parameters: LlamaParseParametersParam | Omit = omit,
        managed_pipeline_id: Optional[str] | Omit = omit,
        metadata_config: Optional[PipelineMetadataConfigParam] | Omit = omit,
        pipeline_type: PipelineType | Omit = omit,
        preset_retrieval_parameters: PresetRetrievalParamsParam | Omit = omit,
        sparse_model_config: Optional[SparseModelConfigParam] | Omit = omit,
        status: Optional[str] | Omit = omit,
        transform_config: Optional[pipeline_upsert_params.TransformConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Upsert a pipeline.

        Updates the pipeline if one with the same name and project already exists,
        otherwise creates a new one.

        Args:
          data_sink: Schema for creating a data sink.

          data_sink_id: Data sink ID. When provided instead of data_sink, the data sink will be looked
              up by ID.

          embedding_model_config_id: Embedding model config ID. When provided instead of embedding_config, the
              embedding model config will be looked up by ID.

          llama_parse_parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          managed_pipeline_id: The ID of the ManagedPipeline this playground pipeline is linked to.

          metadata_config: Metadata configuration for the pipeline.

          pipeline_type: Type of pipeline. Either PLAYGROUND or MANAGED.

          preset_retrieval_parameters: Preset retrieval parameters for the pipeline.

          sparse_model_config: Configuration for sparse embedding models used in hybrid search.

              This allows users to choose between Splade and BM25 models for sparse retrieval
              in managed data sinks.

          status: Status of the pipeline deployment.

          transform_config: Configuration for the transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1/pipelines",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "data_sink": data_sink,
                    "data_sink_id": data_sink_id,
                    "embedding_config": embedding_config,
                    "embedding_model_config_id": embedding_model_config_id,
                    "llama_parse_parameters": llama_parse_parameters,
                    "managed_pipeline_id": managed_pipeline_id,
                    "metadata_config": metadata_config,
                    "pipeline_type": pipeline_type,
                    "preset_retrieval_parameters": preset_retrieval_parameters,
                    "sparse_model_config": sparse_model_config,
                    "status": status,
                    "transform_config": transform_config,
                },
                pipeline_upsert_params.PipelineUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    pipeline_upsert_params.PipelineUpsertParams,
                ),
            ),
            cast_to=Pipeline,
        )


class PipelinesResourceWithRawResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_raw_response_wrapper(
            pipelines.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pipelines.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get = to_raw_response_wrapper(
            pipelines.get,
        )
        self.get_status = to_raw_response_wrapper(
            pipelines.get_status,
        )
        self.upsert = to_raw_response_wrapper(
            pipelines.upsert,
        )

    @cached_property
    def sync(self) -> SyncResourceWithRawResponse:
        return SyncResourceWithRawResponse(self._pipelines.sync)

    @cached_property
    def data_sources(self) -> DataSourcesResourceWithRawResponse:
        return DataSourcesResourceWithRawResponse(self._pipelines.data_sources)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._pipelines.images)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._pipelines.files)

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._pipelines.metadata)

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._pipelines.documents)


class AsyncPipelinesResourceWithRawResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_raw_response_wrapper(
            pipelines.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pipelines.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pipelines.get,
        )
        self.get_status = async_to_raw_response_wrapper(
            pipelines.get_status,
        )
        self.upsert = async_to_raw_response_wrapper(
            pipelines.upsert,
        )

    @cached_property
    def sync(self) -> AsyncSyncResourceWithRawResponse:
        return AsyncSyncResourceWithRawResponse(self._pipelines.sync)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResourceWithRawResponse:
        return AsyncDataSourcesResourceWithRawResponse(self._pipelines.data_sources)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._pipelines.images)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._pipelines.files)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._pipelines.metadata)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._pipelines.documents)


class PipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_streamed_response_wrapper(
            pipelines.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pipelines.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get = to_streamed_response_wrapper(
            pipelines.get,
        )
        self.get_status = to_streamed_response_wrapper(
            pipelines.get_status,
        )
        self.upsert = to_streamed_response_wrapper(
            pipelines.upsert,
        )

    @cached_property
    def sync(self) -> SyncResourceWithStreamingResponse:
        return SyncResourceWithStreamingResponse(self._pipelines.sync)

    @cached_property
    def data_sources(self) -> DataSourcesResourceWithStreamingResponse:
        return DataSourcesResourceWithStreamingResponse(self._pipelines.data_sources)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._pipelines.images)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._pipelines.files)

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._pipelines.metadata)

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._pipelines.documents)


class AsyncPipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_streamed_response_wrapper(
            pipelines.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pipelines.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pipelines.get,
        )
        self.get_status = async_to_streamed_response_wrapper(
            pipelines.get_status,
        )
        self.upsert = async_to_streamed_response_wrapper(
            pipelines.upsert,
        )

    @cached_property
    def sync(self) -> AsyncSyncResourceWithStreamingResponse:
        return AsyncSyncResourceWithStreamingResponse(self._pipelines.sync)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        return AsyncDataSourcesResourceWithStreamingResponse(self._pipelines.data_sources)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._pipelines.images)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._pipelines.files)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._pipelines.metadata)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._pipelines.documents)
