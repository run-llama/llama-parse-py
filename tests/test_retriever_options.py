from __future__ import annotations

import json
from types import SimpleNamespace
from typing import Any

import httpx
import pytest

from llama_cloud.lib.index.retriever import LlamaCloudRetriever


@pytest.mark.filterwarnings("ignore:^deprecated$:DeprecationWarning")
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    "options",
    [
        {},
        {"alpha": 0.0},
        {"enable_reranking": False},
        {"alpha": 0.0, "enable_reranking": False},
        {"alpha": 0.5, "enable_reranking": True},
        {"alpha": None, "enable_reranking": None},
    ],
)
async def test_retriever_preserves_explicit_falsy_options(
    monkeypatch: pytest.MonkeyPatch, asynchronous: bool, options: dict[str, Any]
) -> None:
    monkeypatch.setattr(
        "llama_cloud.lib.index.retriever.resolve_project_and_pipeline",
        lambda *_args: (SimpleNamespace(id="project", name="project"), SimpleNamespace(id="pipeline", name="pipeline")),
    )
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"pipeline_id": "pipeline", "retrieval_nodes": []})

    with httpx.Client(transport=httpx.MockTransport(respond)) as sync_http:
        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as async_http:
            retriever = LlamaCloudRetriever(
                pipeline_id="pipeline",
                api_key="test-key",
                base_url="https://example.com",
                httpx_client=sync_http,
                async_httpx_client=async_http,
                **options,
            )
            result = await retriever.aretrieve("query") if asynchronous else retriever.retrieve("query")
    assert result == []
    assert len(requests) == 1
    payload = json.loads(requests[0].content)
    assert payload["query"] == "query"
    for key in ("alpha", "enable_reranking"):
        if options.get(key) is None:
            assert key not in payload
        else:
            assert payload[key] == options[key]
            assert type(payload[key]) is type(options[key])
