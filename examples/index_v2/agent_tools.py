# ! pip install llama-cloud openai-agents

from __future__ import annotations

import os
import json
import asyncio
from typing import cast

from agents import Agent, Runner, function_tool
from agents.items import ToolCallItem, ToolCallOutputItem
from openai.types.responses.response_input_item_param import FunctionCallOutput
from openai.types.responses.response_text_delta_event import ResponseTextDeltaEvent
from openai.types.responses.response_function_tool_call import ResponseFunctionToolCall

from llama_cloud import AsyncLlamaCloud
from llama_cloud._utils import lru_cache
from llama_cloud.types.beta.retrieval_retrieve_params import Rerank


@lru_cache(maxsize=1)
def get_client() -> AsyncLlamaCloud:
    return AsyncLlamaCloud(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY") or os.getenv("LLAMA_PARSE_API_KEY"),
        base_url=os.getenv("LLAMA_CLOUD_BASE_URL") or os.getenv("LLAMA_PARSE_BASE_URL"),
    )


@lru_cache(maxsize=1)
def get_project_id() -> str | None:
    return os.getenv("LLAMA_CLOUD_PROJECT_ID") or os.getenv("LLAMA_PARSE_PROJECT_ID")


@function_tool
async def list_indexes() -> str:
    """List all available indexes in the current project.

    Returns a formatted string of index names and their export config IDs,
    paginating through all results automatically.
    """
    client = get_client()
    page_token = None
    indexes: list[tuple[str, str]] = []
    while True:
        response = await client.beta.indexes.list(page_token=page_token, project_id=get_project_id())
        indexes.extend([(i.name, i.export_config_id) for i in response.items])
        if response.next_page_token is None:
            break
        page_token = response.next_page_token
    ls = "\n".join([f"- {i[0]} (ID: {i[1]})" for i in indexes])
    return f"Available indexes:\n{ls}"


@function_tool
async def retrieve(
    index_id: str, query: str, top_k: int | None, score_threshold: float | None, rerank_top_n: int | None
) -> str:
    """Run a semantic retrieval query against an index.

    Args:
        index_id: The index to query.
        query: The search query string.
        top_k: Maximum number of results to return. If None, uses the server default.
        score_threshold: Minimum relevance score for results to be included. If None, no threshold is applied.
        rerank_top_n: If set, enables reranking and returns the top N reranked results.

    Returns a formatted string of results with scores, content previews, and metadata.
    """
    client = get_client()
    response = await client.beta.retrieval.retrieve(
        index_id=index_id,
        query=query,
        top_k=top_k,
        score_threshold=score_threshold,
        rerank=Rerank(enabled=rerank_top_n is not None, top_n=rerank_top_n),
    )
    retrieved: list[str] = []
    for i, result in enumerate(response.results):
        r = f"Retrieval result #{i + 1} (Score: {result.score or 'NA'})\n{result.content[:200]}\n"
        if result.metadata:
            r += f"Metadata:\n\n```json\n{json.dumps(result.metadata, indent=2)}\n"
        r += "\n\n---\n\n"
        retrieved.append(r)
    return "\n\n".join(retrieved)


@function_tool
async def find_files(index_id: str, file_name: str | None, file_name_contains: str | None) -> str:
    """Search for files within an index by name.

    Args:
        index_id: The index to search within.
        file_name: Exact file name to match. If None, not used as a filter.
        file_name_contains: Substring to match against file names. If None, not used as a filter.

    Returns a formatted string listing matching file names and their IDs,
    paginating through all results automatically.
    """
    client = get_client()
    files: list[tuple[str, str]] = []
    page_token = None
    while True:
        response = await client.beta.retrieval.find(
            index_id=index_id, file_name=file_name, file_name_contains=file_name_contains, page_token=page_token
        )
        files.extend([(f.file_name, f.file_id) for f in response.items])
        if response.next_page_token is None:
            break
        page_token = response.next_page_token
    ls = "\n".join([f"- {i[0]} (ID: {i[1]})" for i in files])
    return f"Files matching the query:\n{ls}"


@function_tool
async def read_file(index_id: str, file_id: str, offset: int | None, max_length: int | None) -> str:
    """Read the contents of a file from an index.

    Args:
        index_id: The index the file belongs to.
        file_id: The ID of the file to read.
        offset: Character offset to start reading from. Defaults to 0 if None.
        max_length: Maximum number of characters to return. If None, uses the server default.

    Returns the raw file content as a string.
    """
    client = get_client()
    response = await client.beta.retrieval.read(
        index_id=index_id, file_id=file_id, offset=offset or 0, max_length=max_length
    )
    return response.content


@function_tool
async def grep_file(index_id: str, file_id: str, pattern: str, context_chars: int | None, limit: int | None) -> str:
    """Search for a pattern within a specific file using grep.

    Args:
        index_id: The index the file belongs to.
        file_id: The ID of the file to search.
        pattern: The pattern to search for.
        context_chars: Number of surrounding characters to include with each match. If None, uses the server default.
        limit: Maximum number of matches to return per page. If None, uses the server default.

    Returns a formatted string of matches with their character positions,
    paginating through all results automatically.
    """
    client = get_client()
    matches: list[tuple[str, int, int]] = []
    page_token = None
    while True:
        response = await client.beta.retrieval.grep(
            index_id=index_id,
            file_id=file_id,
            pattern=pattern,
            context_chars=context_chars,
            page_size=limit,
            page_token=page_token,
        )
        matches.extend([(m.content, m.start_char, m.end_char) for m in response.items])
        if response.next_page_token is None:
            break
        page_token = response.next_page_token
    ls = "\n".join([f"- {m[0]} (start: {m[1]}, end: {m[2]})" for m in matches])
    return f"Grep matches:\n{ls}"


async def run_agent() -> None:
    agent = Agent(
        name="Index V2 Agent",
        tools=[list_indexes, find_files, retrieve, read_file, grep_file],
        instructions="",
        model="gpt-5.1",
    )
    runner = Runner.run_streamed(
        agent,
        input="List all the files available to you, read one and then search across all of them for 'blue cheese'",
    )
    async for event in runner.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
        elif event.type == "run_item_stream_event" and isinstance(event.item, ToolCallItem):
            print(
                f"\nCalling tool: {cast(ResponseFunctionToolCall, event.item.raw_item).name} with input: {cast(ResponseFunctionToolCall, event.item.raw_item).arguments} (ID: {cast(ResponseFunctionToolCall, event.item.raw_item).call_id})"
            )
        elif event.type == "run_item_stream_event" and isinstance(event.item, ToolCallOutputItem):
            print(
                f"\nResult for tool call {cast(FunctionCallOutput, event.item.raw_item)['call_id']}:\n{event.item.output}"
            )


def main() -> None:
    asyncio.run(run_agent())


if __name__ == "__main__":
    main()
