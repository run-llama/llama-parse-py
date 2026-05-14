# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LlamaCloudError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        beta,
        files,
        extract,
        parsing,
        classify,
        projects,
        pipelines,
        classifier,
        data_sinks,
        retrievers,
        data_sources,
        configurations,
    )
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.extract import ExtractResource, AsyncExtractResource
    from .resources.parsing import ParsingResource, AsyncParsingResource
    from .resources.classify import ClassifyResource, AsyncClassifyResource
    from .resources.projects import ProjectsResource, AsyncProjectsResource
    from .resources.beta.beta import BetaResource, AsyncBetaResource
    from .resources.data_sinks import DataSinksResource, AsyncDataSinksResource
    from .resources.data_sources import DataSourcesResource, AsyncDataSourcesResource
    from .resources.configurations import ConfigurationsResource, AsyncConfigurationsResource
    from .resources.pipelines.pipelines import PipelinesResource, AsyncPipelinesResource
    from .resources.classifier.classifier import ClassifierResource, AsyncClassifierResource
    from .resources.retrievers.retrievers import RetrieversResource, AsyncRetrieversResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LlamaCloud",
    "AsyncLlamaCloud",
    "Client",
    "AsyncClient",
]


class LlamaCloud(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LlamaCloud client instance.

        This automatically infers the `api_key` argument from the `LLAMA_CLOUD_API_KEY` or `LLAMA_PARSE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_CLOUD_API_KEY") or os.environ.get("LLAMA_PARSE_API_KEY")
        if api_key is None:
            raise LlamaCloudError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LLAMA_CLOUD_API_KEY or LLAMA_PARSE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_CLOUD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cloud.llamaindex.ai"

        custom_headers_env = os.environ.get("LLAMA_CLOUD_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def parsing(self) -> ParsingResource:
        from .resources.parsing import ParsingResource

        return ParsingResource(self)

    @cached_property
    def extract(self) -> ExtractResource:
        from .resources.extract import ExtractResource

        return ExtractResource(self)

    @cached_property
    def classifier(self) -> ClassifierResource:
        from .resources.classifier import ClassifierResource

        return ClassifierResource(self)

    @cached_property
    def classify(self) -> ClassifyResource:
        from .resources.classify import ClassifyResource

        return ClassifyResource(self)

    @cached_property
    def configurations(self) -> ConfigurationsResource:
        from .resources.configurations import ConfigurationsResource

        return ConfigurationsResource(self)

    @cached_property
    def projects(self) -> ProjectsResource:
        from .resources.projects import ProjectsResource

        return ProjectsResource(self)

    @cached_property
    def data_sinks(self) -> DataSinksResource:
        from .resources.data_sinks import DataSinksResource

        return DataSinksResource(self)

    @cached_property
    def data_sources(self) -> DataSourcesResource:
        from .resources.data_sources import DataSourcesResource

        return DataSourcesResource(self)

    @cached_property
    def pipelines(self) -> PipelinesResource:
        from .resources.pipelines import PipelinesResource

        return PipelinesResource(self)

    @cached_property
    def retrievers(self) -> RetrieversResource:
        from .resources.retrievers import RetrieversResource

        return RetrieversResource(self)

    @cached_property
    def beta(self) -> BetaResource:
        from .resources.beta import BetaResource

        return BetaResource(self)

    @cached_property
    def with_raw_response(self) -> LlamaCloudWithRawResponse:
        return LlamaCloudWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlamaCloudWithStreamedResponse:
        return LlamaCloudWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLlamaCloud(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLlamaCloud client instance.

        This automatically infers the `api_key` argument from the `LLAMA_CLOUD_API_KEY` or `LLAMA_PARSE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_CLOUD_API_KEY") or os.environ.get("LLAMA_PARSE_API_KEY")
        if api_key is None:
            raise LlamaCloudError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LLAMA_CLOUD_API_KEY or LLAMA_PARSE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_CLOUD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cloud.llamaindex.ai"

        custom_headers_env = os.environ.get("LLAMA_CLOUD_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def parsing(self) -> AsyncParsingResource:
        from .resources.parsing import AsyncParsingResource

        return AsyncParsingResource(self)

    @cached_property
    def extract(self) -> AsyncExtractResource:
        from .resources.extract import AsyncExtractResource

        return AsyncExtractResource(self)

    @cached_property
    def classifier(self) -> AsyncClassifierResource:
        from .resources.classifier import AsyncClassifierResource

        return AsyncClassifierResource(self)

    @cached_property
    def classify(self) -> AsyncClassifyResource:
        from .resources.classify import AsyncClassifyResource

        return AsyncClassifyResource(self)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        from .resources.configurations import AsyncConfigurationsResource

        return AsyncConfigurationsResource(self)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        from .resources.projects import AsyncProjectsResource

        return AsyncProjectsResource(self)

    @cached_property
    def data_sinks(self) -> AsyncDataSinksResource:
        from .resources.data_sinks import AsyncDataSinksResource

        return AsyncDataSinksResource(self)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResource:
        from .resources.data_sources import AsyncDataSourcesResource

        return AsyncDataSourcesResource(self)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResource:
        from .resources.pipelines import AsyncPipelinesResource

        return AsyncPipelinesResource(self)

    @cached_property
    def retrievers(self) -> AsyncRetrieversResource:
        from .resources.retrievers import AsyncRetrieversResource

        return AsyncRetrieversResource(self)

    @cached_property
    def beta(self) -> AsyncBetaResource:
        from .resources.beta import AsyncBetaResource

        return AsyncBetaResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLlamaCloudWithRawResponse:
        return AsyncLlamaCloudWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlamaCloudWithStreamedResponse:
        return AsyncLlamaCloudWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LlamaCloudWithRawResponse:
    _client: LlamaCloud

    def __init__(self, client: LlamaCloud) -> None:
        self._client = client

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def parsing(self) -> parsing.ParsingResourceWithRawResponse:
        from .resources.parsing import ParsingResourceWithRawResponse

        return ParsingResourceWithRawResponse(self._client.parsing)

    @cached_property
    def extract(self) -> extract.ExtractResourceWithRawResponse:
        from .resources.extract import ExtractResourceWithRawResponse

        return ExtractResourceWithRawResponse(self._client.extract)

    @cached_property
    def classifier(self) -> classifier.ClassifierResourceWithRawResponse:
        from .resources.classifier import ClassifierResourceWithRawResponse

        return ClassifierResourceWithRawResponse(self._client.classifier)

    @cached_property
    def classify(self) -> classify.ClassifyResourceWithRawResponse:
        from .resources.classify import ClassifyResourceWithRawResponse

        return ClassifyResourceWithRawResponse(self._client.classify)

    @cached_property
    def configurations(self) -> configurations.ConfigurationsResourceWithRawResponse:
        from .resources.configurations import ConfigurationsResourceWithRawResponse

        return ConfigurationsResourceWithRawResponse(self._client.configurations)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        from .resources.projects import ProjectsResourceWithRawResponse

        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def data_sinks(self) -> data_sinks.DataSinksResourceWithRawResponse:
        from .resources.data_sinks import DataSinksResourceWithRawResponse

        return DataSinksResourceWithRawResponse(self._client.data_sinks)

    @cached_property
    def data_sources(self) -> data_sources.DataSourcesResourceWithRawResponse:
        from .resources.data_sources import DataSourcesResourceWithRawResponse

        return DataSourcesResourceWithRawResponse(self._client.data_sources)

    @cached_property
    def pipelines(self) -> pipelines.PipelinesResourceWithRawResponse:
        from .resources.pipelines import PipelinesResourceWithRawResponse

        return PipelinesResourceWithRawResponse(self._client.pipelines)

    @cached_property
    def retrievers(self) -> retrievers.RetrieversResourceWithRawResponse:
        from .resources.retrievers import RetrieversResourceWithRawResponse

        return RetrieversResourceWithRawResponse(self._client.retrievers)

    @cached_property
    def beta(self) -> beta.BetaResourceWithRawResponse:
        from .resources.beta import BetaResourceWithRawResponse

        return BetaResourceWithRawResponse(self._client.beta)


class AsyncLlamaCloudWithRawResponse:
    _client: AsyncLlamaCloud

    def __init__(self, client: AsyncLlamaCloud) -> None:
        self._client = client

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def parsing(self) -> parsing.AsyncParsingResourceWithRawResponse:
        from .resources.parsing import AsyncParsingResourceWithRawResponse

        return AsyncParsingResourceWithRawResponse(self._client.parsing)

    @cached_property
    def extract(self) -> extract.AsyncExtractResourceWithRawResponse:
        from .resources.extract import AsyncExtractResourceWithRawResponse

        return AsyncExtractResourceWithRawResponse(self._client.extract)

    @cached_property
    def classifier(self) -> classifier.AsyncClassifierResourceWithRawResponse:
        from .resources.classifier import AsyncClassifierResourceWithRawResponse

        return AsyncClassifierResourceWithRawResponse(self._client.classifier)

    @cached_property
    def classify(self) -> classify.AsyncClassifyResourceWithRawResponse:
        from .resources.classify import AsyncClassifyResourceWithRawResponse

        return AsyncClassifyResourceWithRawResponse(self._client.classify)

    @cached_property
    def configurations(self) -> configurations.AsyncConfigurationsResourceWithRawResponse:
        from .resources.configurations import AsyncConfigurationsResourceWithRawResponse

        return AsyncConfigurationsResourceWithRawResponse(self._client.configurations)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        from .resources.projects import AsyncProjectsResourceWithRawResponse

        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def data_sinks(self) -> data_sinks.AsyncDataSinksResourceWithRawResponse:
        from .resources.data_sinks import AsyncDataSinksResourceWithRawResponse

        return AsyncDataSinksResourceWithRawResponse(self._client.data_sinks)

    @cached_property
    def data_sources(self) -> data_sources.AsyncDataSourcesResourceWithRawResponse:
        from .resources.data_sources import AsyncDataSourcesResourceWithRawResponse

        return AsyncDataSourcesResourceWithRawResponse(self._client.data_sources)

    @cached_property
    def pipelines(self) -> pipelines.AsyncPipelinesResourceWithRawResponse:
        from .resources.pipelines import AsyncPipelinesResourceWithRawResponse

        return AsyncPipelinesResourceWithRawResponse(self._client.pipelines)

    @cached_property
    def retrievers(self) -> retrievers.AsyncRetrieversResourceWithRawResponse:
        from .resources.retrievers import AsyncRetrieversResourceWithRawResponse

        return AsyncRetrieversResourceWithRawResponse(self._client.retrievers)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithRawResponse:
        from .resources.beta import AsyncBetaResourceWithRawResponse

        return AsyncBetaResourceWithRawResponse(self._client.beta)


class LlamaCloudWithStreamedResponse:
    _client: LlamaCloud

    def __init__(self, client: LlamaCloud) -> None:
        self._client = client

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def parsing(self) -> parsing.ParsingResourceWithStreamingResponse:
        from .resources.parsing import ParsingResourceWithStreamingResponse

        return ParsingResourceWithStreamingResponse(self._client.parsing)

    @cached_property
    def extract(self) -> extract.ExtractResourceWithStreamingResponse:
        from .resources.extract import ExtractResourceWithStreamingResponse

        return ExtractResourceWithStreamingResponse(self._client.extract)

    @cached_property
    def classifier(self) -> classifier.ClassifierResourceWithStreamingResponse:
        from .resources.classifier import ClassifierResourceWithStreamingResponse

        return ClassifierResourceWithStreamingResponse(self._client.classifier)

    @cached_property
    def classify(self) -> classify.ClassifyResourceWithStreamingResponse:
        from .resources.classify import ClassifyResourceWithStreamingResponse

        return ClassifyResourceWithStreamingResponse(self._client.classify)

    @cached_property
    def configurations(self) -> configurations.ConfigurationsResourceWithStreamingResponse:
        from .resources.configurations import ConfigurationsResourceWithStreamingResponse

        return ConfigurationsResourceWithStreamingResponse(self._client.configurations)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        from .resources.projects import ProjectsResourceWithStreamingResponse

        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def data_sinks(self) -> data_sinks.DataSinksResourceWithStreamingResponse:
        from .resources.data_sinks import DataSinksResourceWithStreamingResponse

        return DataSinksResourceWithStreamingResponse(self._client.data_sinks)

    @cached_property
    def data_sources(self) -> data_sources.DataSourcesResourceWithStreamingResponse:
        from .resources.data_sources import DataSourcesResourceWithStreamingResponse

        return DataSourcesResourceWithStreamingResponse(self._client.data_sources)

    @cached_property
    def pipelines(self) -> pipelines.PipelinesResourceWithStreamingResponse:
        from .resources.pipelines import PipelinesResourceWithStreamingResponse

        return PipelinesResourceWithStreamingResponse(self._client.pipelines)

    @cached_property
    def retrievers(self) -> retrievers.RetrieversResourceWithStreamingResponse:
        from .resources.retrievers import RetrieversResourceWithStreamingResponse

        return RetrieversResourceWithStreamingResponse(self._client.retrievers)

    @cached_property
    def beta(self) -> beta.BetaResourceWithStreamingResponse:
        from .resources.beta import BetaResourceWithStreamingResponse

        return BetaResourceWithStreamingResponse(self._client.beta)


class AsyncLlamaCloudWithStreamedResponse:
    _client: AsyncLlamaCloud

    def __init__(self, client: AsyncLlamaCloud) -> None:
        self._client = client

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def parsing(self) -> parsing.AsyncParsingResourceWithStreamingResponse:
        from .resources.parsing import AsyncParsingResourceWithStreamingResponse

        return AsyncParsingResourceWithStreamingResponse(self._client.parsing)

    @cached_property
    def extract(self) -> extract.AsyncExtractResourceWithStreamingResponse:
        from .resources.extract import AsyncExtractResourceWithStreamingResponse

        return AsyncExtractResourceWithStreamingResponse(self._client.extract)

    @cached_property
    def classifier(self) -> classifier.AsyncClassifierResourceWithStreamingResponse:
        from .resources.classifier import AsyncClassifierResourceWithStreamingResponse

        return AsyncClassifierResourceWithStreamingResponse(self._client.classifier)

    @cached_property
    def classify(self) -> classify.AsyncClassifyResourceWithStreamingResponse:
        from .resources.classify import AsyncClassifyResourceWithStreamingResponse

        return AsyncClassifyResourceWithStreamingResponse(self._client.classify)

    @cached_property
    def configurations(self) -> configurations.AsyncConfigurationsResourceWithStreamingResponse:
        from .resources.configurations import AsyncConfigurationsResourceWithStreamingResponse

        return AsyncConfigurationsResourceWithStreamingResponse(self._client.configurations)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        from .resources.projects import AsyncProjectsResourceWithStreamingResponse

        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def data_sinks(self) -> data_sinks.AsyncDataSinksResourceWithStreamingResponse:
        from .resources.data_sinks import AsyncDataSinksResourceWithStreamingResponse

        return AsyncDataSinksResourceWithStreamingResponse(self._client.data_sinks)

    @cached_property
    def data_sources(self) -> data_sources.AsyncDataSourcesResourceWithStreamingResponse:
        from .resources.data_sources import AsyncDataSourcesResourceWithStreamingResponse

        return AsyncDataSourcesResourceWithStreamingResponse(self._client.data_sources)

    @cached_property
    def pipelines(self) -> pipelines.AsyncPipelinesResourceWithStreamingResponse:
        from .resources.pipelines import AsyncPipelinesResourceWithStreamingResponse

        return AsyncPipelinesResourceWithStreamingResponse(self._client.pipelines)

    @cached_property
    def retrievers(self) -> retrievers.AsyncRetrieversResourceWithStreamingResponse:
        from .resources.retrievers import AsyncRetrieversResourceWithStreamingResponse

        return AsyncRetrieversResourceWithStreamingResponse(self._client.retrievers)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithStreamingResponse:
        from .resources.beta import AsyncBetaResourceWithStreamingResponse

        return AsyncBetaResourceWithStreamingResponse(self._client.beta)


Client = LlamaCloud

AsyncClient = AsyncLlamaCloud
