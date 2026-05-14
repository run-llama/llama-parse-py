# Shared Types

```python
from llama_cloud.types import (
    CloudAstraDBVectorStore,
    CloudAzStorageBlobDataSource,
    CloudAzureAISearchVectorStore,
    CloudBoxDataSource,
    CloudConfluenceDataSource,
    CloudGoogleDriveDataSource,
    CloudJiraDataSource,
    CloudJiraDataSourceV2,
    CloudMilvusVectorStore,
    CloudMongoDBAtlasVectorSearch,
    CloudNotionPageDataSource,
    CloudOneDriveDataSource,
    CloudPineconeVectorStore,
    CloudPostgresVectorStore,
    CloudQdrantVectorStore,
    CloudS3DataSource,
    CloudSharepointDataSource,
    CloudSlackDataSource,
    FailureHandlingConfig,
    PgVectorHnswSettings,
)
```

# Files

Types:

```python
from llama_cloud.types import (
    File,
    PresignedURL,
    FileCreateResponse,
    FileListResponse,
    FileQueryResponse,
)
```

Methods:

- <code title="post /api/v1/beta/files">client.files.<a href="./src/llama_cloud/resources/files.py">create</a>(\*\*<a href="src/llama_cloud/types/file_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /api/v1/beta/files">client.files.<a href="./src/llama_cloud/resources/files.py">list</a>(\*\*<a href="src/llama_cloud/types/file_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/file_list_response.py">SyncPaginatedCursor[FileListResponse]</a></code>
- <code title="delete /api/v1/beta/files/{file_id}">client.files.<a href="./src/llama_cloud/resources/files.py">delete</a>(file_id, \*\*<a href="src/llama_cloud/types/file_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v1/beta/files/{file_id}/content">client.files.<a href="./src/llama_cloud/resources/files.py">get</a>(file_id, \*\*<a href="src/llama_cloud/types/file_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/presigned_url.py">PresignedURL</a></code>
- <code title="post /api/v1/beta/files/query">client.files.<a href="./src/llama_cloud/resources/files.py">query</a>(\*\*<a href="src/llama_cloud/types/file_query_params.py">params</a>) -> <a href="./src/llama_cloud/types/file_query_response.py">FileQueryResponse</a></code>

# Parsing

Types:

```python
from llama_cloud.types import (
    BBox,
    CodeItem,
    FailPageMode,
    FooterItem,
    HeaderItem,
    HeadingItem,
    ImageItem,
    LinkItem,
    ListItem,
    LlamaParseSupportedFileExtensions,
    ParsingJob,
    ParsingLanguages,
    ParsingMode,
    StatusEnum,
    TableItem,
    TextItem,
    ParsingCreateResponse,
    ParsingListResponse,
    ParsingGetResponse,
    ParsingUploadFileResponse,
)
```

Methods:

- <code title="post /api/v2/parse">client.parsing.<a href="./src/llama_cloud/resources/parsing.py">create</a>(\*\*<a href="src/llama_cloud/types/parsing_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/parsing_create_response.py">ParsingCreateResponse</a></code>
- <code title="get /api/v2/parse">client.parsing.<a href="./src/llama_cloud/resources/parsing.py">list</a>(\*\*<a href="src/llama_cloud/types/parsing_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/parsing_list_response.py">SyncPaginatedCursor[ParsingListResponse]</a></code>
- <code title="get /api/v2/parse/{job_id}">client.parsing.<a href="./src/llama_cloud/resources/parsing.py">get</a>(job_id, \*\*<a href="src/llama_cloud/types/parsing_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/parsing_get_response.py">ParsingGetResponse</a></code>

# Extract

Types:

```python
from llama_cloud.types import (
    ExtractConfiguration,
    ExtractJobMetadata,
    ExtractJobUsage,
    ExtractV2Job,
    ExtractV2JobCreate,
    ExtractV2JobQueryResponse,
    ExtractV2SchemaGenerateRequest,
    ExtractV2SchemaValidateRequest,
    ExtractV2SchemaValidateResponse,
    ExtractedFieldMetadata,
)
```

Methods:

- <code title="post /api/v2/extract">client.extract.<a href="./src/llama_cloud/resources/extract.py">create</a>(\*\*<a href="src/llama_cloud/types/extract_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/extract_v2_job.py">ExtractV2Job</a></code>
- <code title="get /api/v2/extract">client.extract.<a href="./src/llama_cloud/resources/extract.py">list</a>(\*\*<a href="src/llama_cloud/types/extract_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/extract_v2_job.py">SyncPaginatedCursor[ExtractV2Job]</a></code>
- <code title="delete /api/v2/extract/{job_id}">client.extract.<a href="./src/llama_cloud/resources/extract.py">delete</a>(job_id, \*\*<a href="src/llama_cloud/types/extract_delete_params.py">params</a>) -> object</code>
- <code title="post /api/v2/extract/schema/generate">client.extract.<a href="./src/llama_cloud/resources/extract.py">generate_schema</a>(\*\*<a href="src/llama_cloud/types/extract_generate_schema_params.py">params</a>) -> <a href="./src/llama_cloud/types/configuration_create.py">ConfigurationCreate</a></code>
- <code title="get /api/v2/extract/{job_id}">client.extract.<a href="./src/llama_cloud/resources/extract.py">get</a>(job_id, \*\*<a href="src/llama_cloud/types/extract_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/extract_v2_job.py">ExtractV2Job</a></code>
- <code title="post /api/v2/extract/schema/validation">client.extract.<a href="./src/llama_cloud/resources/extract.py">validate_schema</a>(\*\*<a href="src/llama_cloud/types/extract_validate_schema_params.py">params</a>) -> <a href="./src/llama_cloud/types/extract_v2_schema_validate_response.py">ExtractV2SchemaValidateResponse</a></code>

# Classifier

## Jobs

Types:

```python
from llama_cloud.types.classifier import (
    ClassifierRule,
    ClassifyJob,
    ClassifyParsingConfiguration,
    JobGetResultsResponse,
)
```

Methods:

- <code title="post /api/v1/classifier/jobs">client.classifier.jobs.<a href="./src/llama_cloud/resources/classifier/jobs.py">create</a>(\*\*<a href="src/llama_cloud/types/classifier/job_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/classifier/classify_job.py">ClassifyJob</a></code>
- <code title="get /api/v1/classifier/jobs">client.classifier.jobs.<a href="./src/llama_cloud/resources/classifier/jobs.py">list</a>(\*\*<a href="src/llama_cloud/types/classifier/job_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/classifier/classify_job.py">SyncPaginatedCursor[ClassifyJob]</a></code>
- <code title="get /api/v1/classifier/jobs/{classify_job_id}">client.classifier.jobs.<a href="./src/llama_cloud/resources/classifier/jobs.py">get</a>(classify_job_id, \*\*<a href="src/llama_cloud/types/classifier/job_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/classifier/classify_job.py">ClassifyJob</a></code>
- <code title="get /api/v1/classifier/jobs/{classify_job_id}/results">client.classifier.jobs.<a href="./src/llama_cloud/resources/classifier/jobs.py">get_results</a>(classify_job_id, \*\*<a href="src/llama_cloud/types/classifier/job_get_results_params.py">params</a>) -> <a href="./src/llama_cloud/types/classifier/job_get_results_response.py">JobGetResultsResponse</a></code>

# Classify

Types:

```python
from llama_cloud.types import (
    ClassifyConfiguration,
    ClassifyCreateRequest,
    ClassifyResult,
    ClassifyCreateResponse,
    ClassifyListResponse,
    ClassifyGetResponse,
)
```

Methods:

- <code title="post /api/v2/classify">client.classify.<a href="./src/llama_cloud/resources/classify.py">create</a>(\*\*<a href="src/llama_cloud/types/classify_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/classify_create_response.py">ClassifyCreateResponse</a></code>
- <code title="get /api/v2/classify">client.classify.<a href="./src/llama_cloud/resources/classify.py">list</a>(\*\*<a href="src/llama_cloud/types/classify_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/classify_list_response.py">SyncPaginatedCursor[ClassifyListResponse]</a></code>
- <code title="get /api/v2/classify/{job_id}">client.classify.<a href="./src/llama_cloud/resources/classify.py">get</a>(job_id, \*\*<a href="src/llama_cloud/types/classify_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/classify_get_response.py">ClassifyGetResponse</a></code>

# Configurations

Types:

```python
from llama_cloud.types import (
    ClassifyV2Parameters,
    ConfigurationCreate,
    ConfigurationResponse,
    ExtractV2Parameters,
    ParseV2Parameters,
    SplitV1Parameters,
    UntypedParameters,
)
```

Methods:

- <code title="post /api/v1/beta/configurations">client.configurations.<a href="./src/llama_cloud/resources/configurations.py">create</a>(\*\*<a href="src/llama_cloud/types/configuration_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/configuration_response.py">ConfigurationResponse</a></code>
- <code title="get /api/v1/beta/configurations/{config_id}">client.configurations.<a href="./src/llama_cloud/resources/configurations.py">retrieve</a>(config_id, \*\*<a href="src/llama_cloud/types/configuration_retrieve_params.py">params</a>) -> <a href="./src/llama_cloud/types/configuration_response.py">ConfigurationResponse</a></code>
- <code title="put /api/v1/beta/configurations/{config_id}">client.configurations.<a href="./src/llama_cloud/resources/configurations.py">update</a>(config_id, \*\*<a href="src/llama_cloud/types/configuration_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/configuration_response.py">ConfigurationResponse</a></code>
- <code title="get /api/v1/beta/configurations">client.configurations.<a href="./src/llama_cloud/resources/configurations.py">list</a>(\*\*<a href="src/llama_cloud/types/configuration_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/configuration_response.py">SyncPaginatedCursor[ConfigurationResponse]</a></code>
- <code title="delete /api/v1/beta/configurations/{config_id}">client.configurations.<a href="./src/llama_cloud/resources/configurations.py">delete</a>(config_id, \*\*<a href="src/llama_cloud/types/configuration_delete_params.py">params</a>) -> None</code>

# Projects

Types:

```python
from llama_cloud.types import Project, ProjectListResponse
```

Methods:

- <code title="get /api/v1/projects">client.projects.<a href="./src/llama_cloud/resources/projects.py">list</a>(\*\*<a href="src/llama_cloud/types/project_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="get /api/v1/projects/{project_id}">client.projects.<a href="./src/llama_cloud/resources/projects.py">get</a>(project_id, \*\*<a href="src/llama_cloud/types/project_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/project.py">Project</a></code>

# DataSinks

Types:

```python
from llama_cloud.types import DataSink, DataSinkListResponse
```

Methods:

- <code title="post /api/v1/data-sinks">client.data_sinks.<a href="./src/llama_cloud/resources/data_sinks.py">create</a>(\*\*<a href="src/llama_cloud/types/data_sink_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/data_sink.py">DataSink</a></code>
- <code title="put /api/v1/data-sinks/{data_sink_id}">client.data_sinks.<a href="./src/llama_cloud/resources/data_sinks.py">update</a>(data_sink_id, \*\*<a href="src/llama_cloud/types/data_sink_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/data_sink.py">DataSink</a></code>
- <code title="get /api/v1/data-sinks">client.data_sinks.<a href="./src/llama_cloud/resources/data_sinks.py">list</a>(\*\*<a href="src/llama_cloud/types/data_sink_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/data_sink_list_response.py">DataSinkListResponse</a></code>
- <code title="delete /api/v1/data-sinks/{data_sink_id}">client.data_sinks.<a href="./src/llama_cloud/resources/data_sinks.py">delete</a>(data_sink_id) -> None</code>
- <code title="get /api/v1/data-sinks/{data_sink_id}">client.data_sinks.<a href="./src/llama_cloud/resources/data_sinks.py">get</a>(data_sink_id) -> <a href="./src/llama_cloud/types/data_sink.py">DataSink</a></code>

# DataSources

Types:

```python
from llama_cloud.types import DataSource, DataSourceReaderVersionMetadata, DataSourceListResponse
```

Methods:

- <code title="post /api/v1/data-sources">client.data_sources.<a href="./src/llama_cloud/resources/data_sources.py">create</a>(\*\*<a href="src/llama_cloud/types/data_source_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/data_source.py">DataSource</a></code>
- <code title="put /api/v1/data-sources/{data_source_id}">client.data_sources.<a href="./src/llama_cloud/resources/data_sources.py">update</a>(data_source_id, \*\*<a href="src/llama_cloud/types/data_source_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/data_source.py">DataSource</a></code>
- <code title="get /api/v1/data-sources">client.data_sources.<a href="./src/llama_cloud/resources/data_sources.py">list</a>(\*\*<a href="src/llama_cloud/types/data_source_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/data_source_list_response.py">DataSourceListResponse</a></code>
- <code title="delete /api/v1/data-sources/{data_source_id}">client.data_sources.<a href="./src/llama_cloud/resources/data_sources.py">delete</a>(data_source_id) -> None</code>
- <code title="get /api/v1/data-sources/{data_source_id}">client.data_sources.<a href="./src/llama_cloud/resources/data_sources.py">get</a>(data_source_id) -> <a href="./src/llama_cloud/types/data_source.py">DataSource</a></code>

# Pipelines

Types:

```python
from llama_cloud.types import (
    AdvancedModeTransformConfig,
    AutoTransformConfig,
    AzureOpenAIEmbedding,
    AzureOpenAIEmbeddingConfig,
    BedrockEmbedding,
    BedrockEmbeddingConfig,
    CohereEmbedding,
    CohereEmbeddingConfig,
    DataSinkCreate,
    GeminiEmbedding,
    GeminiEmbeddingConfig,
    HuggingFaceInferenceAPIEmbedding,
    HuggingFaceInferenceAPIEmbeddingConfig,
    LlamaParseParameters,
    LlmParameters,
    ManagedIngestionStatusResponse,
    MessageRole,
    MetadataFilters,
    OpenAIEmbedding,
    OpenAIEmbeddingConfig,
    PageFigureNodeWithScore,
    PageScreenshotNodeWithScore,
    Pipeline,
    PipelineCreate,
    PipelineMetadataConfig,
    PipelineType,
    PresetRetrievalParams,
    RetrievalMode,
    SparseModelConfig,
    VertexAIEmbeddingConfig,
    VertexTextEmbedding,
    PipelineRetrieveResponse,
    PipelineListResponse,
)
```

Methods:

- <code title="post /api/v1/pipelines">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">create</a>(\*\*<a href="src/llama_cloud/types/pipeline_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipeline.py">Pipeline</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/retrieve">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">retrieve</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipeline_retrieve_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipeline_retrieve_response.py">PipelineRetrieveResponse</a></code>
- <code title="put /api/v1/pipelines/{pipeline_id}">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">update</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipeline_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipeline.py">Pipeline</a></code>
- <code title="get /api/v1/pipelines">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">list</a>(\*\*<a href="src/llama_cloud/types/pipeline_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipeline_list_response.py">PipelineListResponse</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">delete</a>(pipeline_id) -> None</code>
- <code title="get /api/v1/pipelines/{pipeline_id}">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">get</a>(pipeline_id) -> <a href="./src/llama_cloud/types/pipeline.py">Pipeline</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/status">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">get_status</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipeline_get_status_params.py">params</a>) -> <a href="./src/llama_cloud/types/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>
- <code title="put /api/v1/pipelines">client.pipelines.<a href="./src/llama_cloud/resources/pipelines/pipelines.py">upsert</a>(\*\*<a href="src/llama_cloud/types/pipeline_upsert_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipeline.py">Pipeline</a></code>

## Sync

Methods:

- <code title="post /api/v1/pipelines/{pipeline_id}/sync">client.pipelines.sync.<a href="./src/llama_cloud/resources/pipelines/sync.py">create</a>(pipeline_id) -> <a href="./src/llama_cloud/types/pipeline.py">Pipeline</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/sync/cancel">client.pipelines.sync.<a href="./src/llama_cloud/resources/pipelines/sync.py">cancel</a>(pipeline_id) -> <a href="./src/llama_cloud/types/pipeline.py">Pipeline</a></code>

## DataSources

Types:

```python
from llama_cloud.types.pipelines import (
    PipelineDataSource,
    DataSourceGetDataSourcesResponse,
    DataSourceUpdateDataSourcesResponse,
)
```

Methods:

- <code title="put /api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}">client.pipelines.data_sources.<a href="./src/llama_cloud/resources/pipelines/data_sources.py">update</a>(data_source_id, \*, pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/data_source_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/pipeline_data_source.py">PipelineDataSource</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/data-sources">client.pipelines.data_sources.<a href="./src/llama_cloud/resources/pipelines/data_sources.py">get_data_sources</a>(pipeline_id) -> <a href="./src/llama_cloud/types/pipelines/data_source_get_data_sources_response.py">DataSourceGetDataSourcesResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status">client.pipelines.data_sources.<a href="./src/llama_cloud/resources/pipelines/data_sources.py">get_status</a>(data_source_id, \*, pipeline_id) -> <a href="./src/llama_cloud/types/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync">client.pipelines.data_sources.<a href="./src/llama_cloud/resources/pipelines/data_sources.py">sync</a>(data_source_id, \*, pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/data_source_sync_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipeline.py">Pipeline</a></code>
- <code title="put /api/v1/pipelines/{pipeline_id}/data-sources">client.pipelines.data_sources.<a href="./src/llama_cloud/resources/pipelines/data_sources.py">update_data_sources</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/data_source_update_data_sources_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/data_source_update_data_sources_response.py">DataSourceUpdateDataSourcesResponse</a></code>

## Images

Types:

```python
from llama_cloud.types.pipelines import (
    ImageListPageFiguresResponse,
    ImageListPageScreenshotsResponse,
)
```

Methods:

- <code title="get /api/v1/files/{id}/page-figures/{page_index}/{figure_name}">client.pipelines.images.<a href="./src/llama_cloud/resources/pipelines/images.py">get_page_figure</a>(figure_name, \*, id, page_index, \*\*<a href="src/llama_cloud/types/pipelines/image_get_page_figure_params.py">params</a>) -> object</code>
- <code title="get /api/v1/files/{id}/page_screenshots/{page_index}">client.pipelines.images.<a href="./src/llama_cloud/resources/pipelines/images.py">get_page_screenshot</a>(page_index, \*, id, \*\*<a href="src/llama_cloud/types/pipelines/image_get_page_screenshot_params.py">params</a>) -> object</code>
- <code title="get /api/v1/files/{id}/page-figures">client.pipelines.images.<a href="./src/llama_cloud/resources/pipelines/images.py">list_page_figures</a>(id, \*\*<a href="src/llama_cloud/types/pipelines/image_list_page_figures_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/image_list_page_figures_response.py">ImageListPageFiguresResponse</a></code>
- <code title="get /api/v1/files/{id}/page_screenshots">client.pipelines.images.<a href="./src/llama_cloud/resources/pipelines/images.py">list_page_screenshots</a>(id, \*\*<a href="src/llama_cloud/types/pipelines/image_list_page_screenshots_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/image_list_page_screenshots_response.py">ImageListPageScreenshotsResponse</a></code>

## Files

Types:

```python
from llama_cloud.types.pipelines import (
    PipelineFile,
    FileCreateResponse,
    FileGetStatusCountsResponse,
)
```

Methods:

- <code title="put /api/v1/pipelines/{pipeline_id}/files">client.pipelines.files.<a href="./src/llama_cloud/resources/pipelines/files.py">create</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/file_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/file_create_response.py">FileCreateResponse</a></code>
- <code title="put /api/v1/pipelines/{pipeline_id}/files/{file_id}">client.pipelines.files.<a href="./src/llama_cloud/resources/pipelines/files.py">update</a>(file_id, \*, pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/file_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/pipeline_file.py">PipelineFile</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/files2">client.pipelines.files.<a href="./src/llama_cloud/resources/pipelines/files.py">list</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/file_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/pipeline_file.py">SyncPaginatedPipelineFiles[PipelineFile]</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}/files/{file_id}">client.pipelines.files.<a href="./src/llama_cloud/resources/pipelines/files.py">delete</a>(file_id, \*, pipeline_id) -> None</code>
- <code title="get /api/v1/pipelines/{pipeline_id}/files/{file_id}/status">client.pipelines.files.<a href="./src/llama_cloud/resources/pipelines/files.py">get_status</a>(file_id, \*, pipeline_id) -> <a href="./src/llama_cloud/types/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/files/status-counts">client.pipelines.files.<a href="./src/llama_cloud/resources/pipelines/files.py">get_status_counts</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/file_get_status_counts_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/file_get_status_counts_response.py">FileGetStatusCountsResponse</a></code>

## Metadata

Types:

```python
from llama_cloud.types.pipelines import MetadataCreateResponse
```

Methods:

- <code title="put /api/v1/pipelines/{pipeline_id}/metadata">client.pipelines.metadata.<a href="./src/llama_cloud/resources/pipelines/metadata.py">create</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/metadata_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/metadata_create_response.py">MetadataCreateResponse</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}/metadata">client.pipelines.metadata.<a href="./src/llama_cloud/resources/pipelines/metadata.py">delete_all</a>(pipeline_id) -> None</code>

## Documents

Types:

```python
from llama_cloud.types.pipelines import (
    CloudDocument,
    CloudDocumentCreate,
    TextNode,
    DocumentCreateResponse,
    DocumentGetChunksResponse,
    DocumentUpsertResponse,
)
```

Methods:

- <code title="post /api/v1/pipelines/{pipeline_id}/documents">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">create</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/document_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/paginated">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">list</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/document_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/cloud_document.py">SyncPaginatedCloudDocuments[CloudDocument]</a></code>
- <code title="delete /api/v1/pipelines/{pipeline_id}/documents/{document_id}">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">delete</a>(document_id, \*, pipeline_id) -> None</code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/{document_id}">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">get</a>(document_id, \*, pipeline_id) -> <a href="./src/llama_cloud/types/pipelines/cloud_document.py">CloudDocument</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">get_chunks</a>(document_id, \*, pipeline_id) -> <a href="./src/llama_cloud/types/pipelines/document_get_chunks_response.py">DocumentGetChunksResponse</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/documents/{document_id}/status">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">get_status</a>(document_id, \*, pipeline_id) -> <a href="./src/llama_cloud/types/managed_ingestion_status_response.py">ManagedIngestionStatusResponse</a></code>
- <code title="post /api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">sync</a>(document_id, \*, pipeline_id) -> object</code>
- <code title="put /api/v1/pipelines/{pipeline_id}/documents">client.pipelines.documents.<a href="./src/llama_cloud/resources/pipelines/documents.py">upsert</a>(pipeline_id, \*\*<a href="src/llama_cloud/types/pipelines/document_upsert_params.py">params</a>) -> <a href="./src/llama_cloud/types/pipelines/document_upsert_response.py">DocumentUpsertResponse</a></code>

# Retrievers

Types:

```python
from llama_cloud.types import (
    CompositeRetrievalMode,
    CompositeRetrievalResult,
    ReRankConfig,
    Retriever,
    RetrieverCreate,
    RetrieverPipeline,
    RetrieverListResponse,
)
```

Methods:

- <code title="post /api/v1/retrievers">client.retrievers.<a href="./src/llama_cloud/resources/retrievers/retrievers.py">create</a>(\*\*<a href="src/llama_cloud/types/retriever_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/retriever.py">Retriever</a></code>
- <code title="put /api/v1/retrievers/{retriever_id}">client.retrievers.<a href="./src/llama_cloud/resources/retrievers/retrievers.py">update</a>(retriever_id, \*\*<a href="src/llama_cloud/types/retriever_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/retriever.py">Retriever</a></code>
- <code title="get /api/v1/retrievers">client.retrievers.<a href="./src/llama_cloud/resources/retrievers/retrievers.py">list</a>(\*\*<a href="src/llama_cloud/types/retriever_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/retriever_list_response.py">RetrieverListResponse</a></code>
- <code title="delete /api/v1/retrievers/{retriever_id}">client.retrievers.<a href="./src/llama_cloud/resources/retrievers/retrievers.py">delete</a>(retriever_id, \*\*<a href="src/llama_cloud/types/retriever_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v1/retrievers/{retriever_id}">client.retrievers.<a href="./src/llama_cloud/resources/retrievers/retrievers.py">get</a>(retriever_id, \*\*<a href="src/llama_cloud/types/retriever_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/retriever.py">Retriever</a></code>
- <code title="post /api/v1/retrievers/retrieve">client.retrievers.<a href="./src/llama_cloud/resources/retrievers/retrievers.py">search</a>(\*\*<a href="src/llama_cloud/types/retriever_search_params.py">params</a>) -> <a href="./src/llama_cloud/types/composite_retrieval_result.py">CompositeRetrievalResult</a></code>
- <code title="put /api/v1/retrievers">client.retrievers.<a href="./src/llama_cloud/resources/retrievers/retrievers.py">upsert</a>(\*\*<a href="src/llama_cloud/types/retriever_upsert_params.py">params</a>) -> <a href="./src/llama_cloud/types/retriever.py">Retriever</a></code>

## Retriever

Methods:

- <code title="post /api/v1/retrievers/{retriever_id}/retrieve">client.retrievers.retriever.<a href="./src/llama_cloud/resources/retrievers/retriever.py">search</a>(retriever_id, \*\*<a href="src/llama_cloud/types/retrievers/retriever_search_params.py">params</a>) -> <a href="./src/llama_cloud/types/composite_retrieval_result.py">CompositeRetrievalResult</a></code>

# Beta

## AgentData

Types:

```python
from llama_cloud.types.beta import (
    AgentData,
    AgentDataDeleteResponse,
    AgentDataAggregateResponse,
    AgentDataDeleteByQueryResponse,
)
```

Methods:

- <code title="post /api/v1/beta/agent-data">client.beta.agent_data.<a href="./src/llama_cloud/resources/beta/agent_data.py">create</a>(\*\*<a href="src/llama_cloud/types/beta/agent_data_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/agent_data.py">AgentData</a></code>
- <code title="put /api/v1/beta/agent-data/{item_id}">client.beta.agent_data.<a href="./src/llama_cloud/resources/beta/agent_data.py">update</a>(item_id, \*\*<a href="src/llama_cloud/types/beta/agent_data_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/agent_data.py">AgentData</a></code>
- <code title="delete /api/v1/beta/agent-data/{item_id}">client.beta.agent_data.<a href="./src/llama_cloud/resources/beta/agent_data.py">delete</a>(item_id, \*\*<a href="src/llama_cloud/types/beta/agent_data_delete_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/agent_data_delete_response.py">AgentDataDeleteResponse</a></code>
- <code title="post /api/v1/beta/agent-data/:aggregate">client.beta.agent_data.<a href="./src/llama_cloud/resources/beta/agent_data.py">aggregate</a>(\*\*<a href="src/llama_cloud/types/beta/agent_data_aggregate_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/agent_data_aggregate_response.py">SyncPaginatedCursorPost[AgentDataAggregateResponse]</a></code>
- <code title="post /api/v1/beta/agent-data/:delete">client.beta.agent_data.<a href="./src/llama_cloud/resources/beta/agent_data.py">delete_by_query</a>(\*\*<a href="src/llama_cloud/types/beta/agent_data_delete_by_query_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/agent_data_delete_by_query_response.py">AgentDataDeleteByQueryResponse</a></code>
- <code title="get /api/v1/beta/agent-data/{item_id}">client.beta.agent_data.<a href="./src/llama_cloud/resources/beta/agent_data.py">get</a>(item_id, \*\*<a href="src/llama_cloud/types/beta/agent_data_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/agent_data.py">AgentData</a></code>
- <code title="post /api/v1/beta/agent-data/:search">client.beta.agent_data.<a href="./src/llama_cloud/resources/beta/agent_data.py">search</a>(\*\*<a href="src/llama_cloud/types/beta/agent_data_search_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/agent_data.py">SyncPaginatedCursorPost[AgentData]</a></code>

## Sheets

Types:

```python
from llama_cloud.types.beta import SheetsJob, SheetsParsingConfig
```

Methods:

- <code title="post /api/v1/beta/sheets/jobs">client.beta.sheets.<a href="./src/llama_cloud/resources/beta/sheets.py">create</a>(\*\*<a href="src/llama_cloud/types/beta/sheet_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/sheets_job.py">SheetsJob</a></code>
- <code title="get /api/v1/beta/sheets/jobs">client.beta.sheets.<a href="./src/llama_cloud/resources/beta/sheets.py">list</a>(\*\*<a href="src/llama_cloud/types/beta/sheet_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/sheets_job.py">SyncPaginatedCursor[SheetsJob]</a></code>
- <code title="delete /api/v1/beta/sheets/jobs/{spreadsheet_job_id}">client.beta.sheets.<a href="./src/llama_cloud/resources/beta/sheets.py">delete_job</a>(spreadsheet_job_id, \*\*<a href="src/llama_cloud/types/beta/sheet_delete_job_params.py">params</a>) -> object</code>
- <code title="get /api/v1/beta/sheets/jobs/{spreadsheet_job_id}">client.beta.sheets.<a href="./src/llama_cloud/resources/beta/sheets.py">get</a>(spreadsheet_job_id, \*\*<a href="src/llama_cloud/types/beta/sheet_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/sheets_job.py">SheetsJob</a></code>
- <code title="get /api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}">client.beta.sheets.<a href="./src/llama_cloud/resources/beta/sheets.py">get_result_table</a>(region_type, \*, spreadsheet_job_id, region_id, \*\*<a href="src/llama_cloud/types/beta/sheet_get_result_table_params.py">params</a>) -> <a href="./src/llama_cloud/types/presigned_url.py">PresignedURL</a></code>

## Directories

Types:

```python
from llama_cloud.types.beta import (
    DirectoryCreateResponse,
    DirectoryUpdateResponse,
    DirectoryListResponse,
    DirectoryGetResponse,
)
```

Methods:

- <code title="post /api/v1/beta/directories">client.beta.directories.<a href="./src/llama_cloud/resources/beta/directories/directories.py">create</a>(\*\*<a href="src/llama_cloud/types/beta/directory_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directory_create_response.py">DirectoryCreateResponse</a></code>
- <code title="patch /api/v1/beta/directories/{directory_id}">client.beta.directories.<a href="./src/llama_cloud/resources/beta/directories/directories.py">update</a>(directory_id, \*\*<a href="src/llama_cloud/types/beta/directory_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directory_update_response.py">DirectoryUpdateResponse</a></code>
- <code title="get /api/v1/beta/directories">client.beta.directories.<a href="./src/llama_cloud/resources/beta/directories/directories.py">list</a>(\*\*<a href="src/llama_cloud/types/beta/directory_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directory_list_response.py">SyncPaginatedCursor[DirectoryListResponse]</a></code>
- <code title="delete /api/v1/beta/directories/{directory_id}">client.beta.directories.<a href="./src/llama_cloud/resources/beta/directories/directories.py">delete</a>(directory_id, \*\*<a href="src/llama_cloud/types/beta/directory_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v1/beta/directories/{directory_id}">client.beta.directories.<a href="./src/llama_cloud/resources/beta/directories/directories.py">get</a>(directory_id, \*\*<a href="src/llama_cloud/types/beta/directory_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directory_get_response.py">DirectoryGetResponse</a></code>

### Files

Types:

```python
from llama_cloud.types.beta.directories import (
    FileUpdateResponse,
    FileListResponse,
    FileAddResponse,
    FileGetResponse,
    FileUploadResponse,
)
```

Methods:

- <code title="patch /api/v1/beta/directories/{directory_id}/files/{directory_file_id}">client.beta.directories.files.<a href="./src/llama_cloud/resources/beta/directories/files.py">update</a>(directory_file_id, \*, path_directory_id, \*\*<a href="src/llama_cloud/types/beta/directories/file_update_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directories/file_update_response.py">FileUpdateResponse</a></code>
- <code title="get /api/v1/beta/directories/{directory_id}/files">client.beta.directories.files.<a href="./src/llama_cloud/resources/beta/directories/files.py">list</a>(directory_id, \*\*<a href="src/llama_cloud/types/beta/directories/file_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directories/file_list_response.py">SyncPaginatedCursor[FileListResponse]</a></code>
- <code title="delete /api/v1/beta/directories/{directory_id}/files/{directory_file_id}">client.beta.directories.files.<a href="./src/llama_cloud/resources/beta/directories/files.py">delete</a>(directory_file_id, \*, directory_id, \*\*<a href="src/llama_cloud/types/beta/directories/file_delete_params.py">params</a>) -> None</code>
- <code title="post /api/v1/beta/directories/{directory_id}/files">client.beta.directories.files.<a href="./src/llama_cloud/resources/beta/directories/files.py">add</a>(directory_id, \*\*<a href="src/llama_cloud/types/beta/directories/file_add_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directories/file_add_response.py">FileAddResponse</a></code>
- <code title="get /api/v1/beta/directories/{directory_id}/files/{directory_file_id}">client.beta.directories.files.<a href="./src/llama_cloud/resources/beta/directories/files.py">get</a>(directory_file_id, \*, directory_id, \*\*<a href="src/llama_cloud/types/beta/directories/file_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directories/file_get_response.py">FileGetResponse</a></code>
- <code title="post /api/v1/beta/directories/{directory_id}/files/upload">client.beta.directories.files.<a href="./src/llama_cloud/resources/beta/directories/files.py">upload</a>(directory_id, \*\*<a href="src/llama_cloud/types/beta/directories/file_upload_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/directories/file_upload_response.py">FileUploadResponse</a></code>

## Batch

Types:

```python
from llama_cloud.types.beta import (
    BatchCreateResponse,
    BatchListResponse,
    BatchCancelResponse,
    BatchGetStatusResponse,
)
```

Methods:

- <code title="post /api/v1/beta/batch-processing">client.beta.batch.<a href="./src/llama_cloud/resources/beta/batch/batch.py">create</a>(\*\*<a href="src/llama_cloud/types/beta/batch_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="get /api/v1/beta/batch-processing">client.beta.batch.<a href="./src/llama_cloud/resources/beta/batch/batch.py">list</a>(\*\*<a href="src/llama_cloud/types/beta/batch_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/batch_list_response.py">SyncPaginatedBatchItems[BatchListResponse]</a></code>
- <code title="post /api/v1/beta/batch-processing/{job_id}/cancel">client.beta.batch.<a href="./src/llama_cloud/resources/beta/batch/batch.py">cancel</a>(job_id, \*\*<a href="src/llama_cloud/types/beta/batch_cancel_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/batch_cancel_response.py">BatchCancelResponse</a></code>
- <code title="get /api/v1/beta/batch-processing/{job_id}">client.beta.batch.<a href="./src/llama_cloud/resources/beta/batch/batch.py">get_status</a>(job_id, \*\*<a href="src/llama_cloud/types/beta/batch_get_status_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/batch_get_status_response.py">BatchGetStatusResponse</a></code>

### JobItems

Types:

```python
from llama_cloud.types.beta.batch import JobItemListResponse, JobItemGetProcessingResultsResponse
```

Methods:

- <code title="get /api/v1/beta/batch-processing/{job_id}/items">client.beta.batch.job_items.<a href="./src/llama_cloud/resources/beta/batch/job_items.py">list</a>(job_id, \*\*<a href="src/llama_cloud/types/beta/batch/job_item_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/batch/job_item_list_response.py">SyncPaginatedBatchItems[JobItemListResponse]</a></code>
- <code title="get /api/v1/beta/batch-processing/items/{item_id}/processing-results">client.beta.batch.job_items.<a href="./src/llama_cloud/resources/beta/batch/job_items.py">get_processing_results</a>(item_id, \*\*<a href="src/llama_cloud/types/beta/batch/job_item_get_processing_results_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/batch/job_item_get_processing_results_response.py">JobItemGetProcessingResultsResponse</a></code>

## Split

Types:

```python
from llama_cloud.types.beta import (
    SplitCategory,
    SplitDocumentInput,
    SplitResultResponse,
    SplitSegmentResponse,
    SplitCreateResponse,
    SplitListResponse,
    SplitGetResponse,
)
```

Methods:

- <code title="post /api/v1/beta/split/jobs">client.beta.split.<a href="./src/llama_cloud/resources/beta/split.py">create</a>(\*\*<a href="src/llama_cloud/types/beta/split_create_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/split_create_response.py">SplitCreateResponse</a></code>
- <code title="get /api/v1/beta/split/jobs">client.beta.split.<a href="./src/llama_cloud/resources/beta/split.py">list</a>(\*\*<a href="src/llama_cloud/types/beta/split_list_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/split_list_response.py">SyncPaginatedCursor[SplitListResponse]</a></code>
- <code title="get /api/v1/beta/split/jobs/{split_job_id}">client.beta.split.<a href="./src/llama_cloud/resources/beta/split.py">get</a>(split_job_id, \*\*<a href="src/llama_cloud/types/beta/split_get_params.py">params</a>) -> <a href="./src/llama_cloud/types/beta/split_get_response.py">SplitGetResponse</a></code>
