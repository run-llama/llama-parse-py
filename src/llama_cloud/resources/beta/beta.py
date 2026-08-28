# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from .split import (
    SplitResource,
    AsyncSplitResource,
    SplitResourceWithRawResponse,
    AsyncSplitResourceWithRawResponse,
    SplitResourceWithStreamingResponse,
    AsyncSplitResourceWithStreamingResponse,
)
from .indexes import (
    IndexesResource,
    AsyncIndexesResource,
    IndexesResourceWithRawResponse,
    AsyncIndexesResourceWithRawResponse,
    IndexesResourceWithStreamingResponse,
    AsyncIndexesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .retrieval import (
    RetrievalResource,
    AsyncRetrievalResource,
    RetrievalResourceWithRawResponse,
    AsyncRetrievalResourceWithRawResponse,
    RetrievalResourceWithStreamingResponse,
    AsyncRetrievalResourceWithStreamingResponse,
)
from .agent_data import (
    AgentDataResource,
    AsyncAgentDataResource,
    AgentDataResourceWithRawResponse,
    AsyncAgentDataResourceWithRawResponse,
    AgentDataResourceWithStreamingResponse,
    AsyncAgentDataResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
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
    def indexes(self) -> IndexesResource:
        return IndexesResource(self._client)

    @cached_property
    def retrieval(self) -> RetrievalResource:
        return RetrievalResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def agent_data(self) -> AgentDataResource:
        return AgentDataResource(self._client)

    @cached_property
    def directories(self) -> DirectoriesResource:
        return DirectoriesResource(self._client)

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
    def indexes(self) -> AsyncIndexesResource:
        return AsyncIndexesResource(self._client)

    @cached_property
    def retrieval(self) -> AsyncRetrievalResource:
        return AsyncRetrievalResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def agent_data(self) -> AsyncAgentDataResource:
        return AsyncAgentDataResource(self._client)

    @cached_property
    def directories(self) -> AsyncDirectoriesResource:
        return AsyncDirectoriesResource(self._client)

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
    def indexes(self) -> IndexesResourceWithRawResponse:
        return IndexesResourceWithRawResponse(self._beta.indexes)

    @cached_property
    def retrieval(self) -> RetrievalResourceWithRawResponse:
        return RetrievalResourceWithRawResponse(self._beta.retrieval)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._beta.chat)

    @cached_property
    def agent_data(self) -> AgentDataResourceWithRawResponse:
        return AgentDataResourceWithRawResponse(self._beta.agent_data)

    @cached_property
    def directories(self) -> DirectoriesResourceWithRawResponse:
        return DirectoriesResourceWithRawResponse(self._beta.directories)

    @cached_property
    def split(self) -> SplitResourceWithRawResponse:
        return SplitResourceWithRawResponse(self._beta.split)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithRawResponse:
        return AsyncIndexesResourceWithRawResponse(self._beta.indexes)

    @cached_property
    def retrieval(self) -> AsyncRetrievalResourceWithRawResponse:
        return AsyncRetrievalResourceWithRawResponse(self._beta.retrieval)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._beta.chat)

    @cached_property
    def agent_data(self) -> AsyncAgentDataResourceWithRawResponse:
        return AsyncAgentDataResourceWithRawResponse(self._beta.agent_data)

    @cached_property
    def directories(self) -> AsyncDirectoriesResourceWithRawResponse:
        return AsyncDirectoriesResourceWithRawResponse(self._beta.directories)

    @cached_property
    def split(self) -> AsyncSplitResourceWithRawResponse:
        return AsyncSplitResourceWithRawResponse(self._beta.split)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def indexes(self) -> IndexesResourceWithStreamingResponse:
        return IndexesResourceWithStreamingResponse(self._beta.indexes)

    @cached_property
    def retrieval(self) -> RetrievalResourceWithStreamingResponse:
        return RetrievalResourceWithStreamingResponse(self._beta.retrieval)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._beta.chat)

    @cached_property
    def agent_data(self) -> AgentDataResourceWithStreamingResponse:
        return AgentDataResourceWithStreamingResponse(self._beta.agent_data)

    @cached_property
    def directories(self) -> DirectoriesResourceWithStreamingResponse:
        return DirectoriesResourceWithStreamingResponse(self._beta.directories)

    @cached_property
    def split(self) -> SplitResourceWithStreamingResponse:
        return SplitResourceWithStreamingResponse(self._beta.split)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithStreamingResponse:
        return AsyncIndexesResourceWithStreamingResponse(self._beta.indexes)

    @cached_property
    def retrieval(self) -> AsyncRetrievalResourceWithStreamingResponse:
        return AsyncRetrievalResourceWithStreamingResponse(self._beta.retrieval)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._beta.chat)

    @cached_property
    def agent_data(self) -> AsyncAgentDataResourceWithStreamingResponse:
        return AsyncAgentDataResourceWithStreamingResponse(self._beta.agent_data)

    @cached_property
    def directories(self) -> AsyncDirectoriesResourceWithStreamingResponse:
        return AsyncDirectoriesResourceWithStreamingResponse(self._beta.directories)

    @cached_property
    def split(self) -> AsyncSplitResourceWithStreamingResponse:
        return AsyncSplitResourceWithStreamingResponse(self._beta.split)
