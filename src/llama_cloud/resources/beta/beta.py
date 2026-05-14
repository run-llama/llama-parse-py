# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .split import (
    SplitResource,
    AsyncSplitResource,
    SplitResourceWithRawResponse,
    AsyncSplitResourceWithRawResponse,
    SplitResourceWithStreamingResponse,
    AsyncSplitResourceWithStreamingResponse,
)
from .sheets import (
    SheetsResource,
    AsyncSheetsResource,
    SheetsResourceWithRawResponse,
    AsyncSheetsResourceWithRawResponse,
    SheetsResourceWithStreamingResponse,
    AsyncSheetsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .agent_data import (
    AgentDataResource,
    AsyncAgentDataResource,
    AgentDataResourceWithRawResponse,
    AsyncAgentDataResourceWithRawResponse,
    AgentDataResourceWithStreamingResponse,
    AsyncAgentDataResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .batch.batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .directories.directories import (
    DirectoriesResource,
    AsyncDirectoriesResource,
    DirectoriesResourceWithRawResponse,
    AsyncDirectoriesResourceWithRawResponse,
    DirectoriesResourceWithStreamingResponse,
    AsyncDirectoriesResourceWithStreamingResponse,
)

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def agent_data(self) -> AgentDataResource:
        return AgentDataResource(self._client)

    @cached_property
    def sheets(self) -> SheetsResource:
        return SheetsResource(self._client)

    @cached_property
    def directories(self) -> DirectoriesResource:
        return DirectoriesResource(self._client)

    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def split(self) -> SplitResource:
        return SplitResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def agent_data(self) -> AsyncAgentDataResource:
        return AsyncAgentDataResource(self._client)

    @cached_property
    def sheets(self) -> AsyncSheetsResource:
        return AsyncSheetsResource(self._client)

    @cached_property
    def directories(self) -> AsyncDirectoriesResource:
        return AsyncDirectoriesResource(self._client)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def split(self) -> AsyncSplitResource:
        return AsyncSplitResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def agent_data(self) -> AgentDataResourceWithRawResponse:
        return AgentDataResourceWithRawResponse(self._beta.agent_data)

    @cached_property
    def sheets(self) -> SheetsResourceWithRawResponse:
        return SheetsResourceWithRawResponse(self._beta.sheets)

    @cached_property
    def directories(self) -> DirectoriesResourceWithRawResponse:
        return DirectoriesResourceWithRawResponse(self._beta.directories)

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._beta.batch)

    @cached_property
    def split(self) -> SplitResourceWithRawResponse:
        return SplitResourceWithRawResponse(self._beta.split)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def agent_data(self) -> AsyncAgentDataResourceWithRawResponse:
        return AsyncAgentDataResourceWithRawResponse(self._beta.agent_data)

    @cached_property
    def sheets(self) -> AsyncSheetsResourceWithRawResponse:
        return AsyncSheetsResourceWithRawResponse(self._beta.sheets)

    @cached_property
    def directories(self) -> AsyncDirectoriesResourceWithRawResponse:
        return AsyncDirectoriesResourceWithRawResponse(self._beta.directories)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._beta.batch)

    @cached_property
    def split(self) -> AsyncSplitResourceWithRawResponse:
        return AsyncSplitResourceWithRawResponse(self._beta.split)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def agent_data(self) -> AgentDataResourceWithStreamingResponse:
        return AgentDataResourceWithStreamingResponse(self._beta.agent_data)

    @cached_property
    def sheets(self) -> SheetsResourceWithStreamingResponse:
        return SheetsResourceWithStreamingResponse(self._beta.sheets)

    @cached_property
    def directories(self) -> DirectoriesResourceWithStreamingResponse:
        return DirectoriesResourceWithStreamingResponse(self._beta.directories)

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._beta.batch)

    @cached_property
    def split(self) -> SplitResourceWithStreamingResponse:
        return SplitResourceWithStreamingResponse(self._beta.split)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def agent_data(self) -> AsyncAgentDataResourceWithStreamingResponse:
        return AsyncAgentDataResourceWithStreamingResponse(self._beta.agent_data)

    @cached_property
    def sheets(self) -> AsyncSheetsResourceWithStreamingResponse:
        return AsyncSheetsResourceWithStreamingResponse(self._beta.sheets)

    @cached_property
    def directories(self) -> AsyncDirectoriesResourceWithStreamingResponse:
        return AsyncDirectoriesResourceWithStreamingResponse(self._beta.directories)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._beta.batch)

    @cached_property
    def split(self) -> AsyncSplitResourceWithStreamingResponse:
        return AsyncSplitResourceWithStreamingResponse(self._beta.split)
