# Llama Cloud Python SDK

[![PyPI version](https://img.shields.io/pypi/v/llama_cloud.svg?label=pypi%20(stable))](https://pypi.org/project/llama_cloud/)

The official Python SDK for [LlamaParse](https://cloud.llamaindex.ai) - the enterprise platform for agentic OCR and document processing.

With this SDK, create powerful workflows across many features:

- **Parse** - Agentic OCR and parsing for 130+ formats
- **Extract** - Structured data extraction with custom schemas
- **Classify** - Document categorization with natural-language rules
- **Agents** - Deploy document agents as APIs
- **Index** - Document ingestion and embedding for RAG

## Documentation

- [Get an API Key](https://cloud.llamaindex.ai)
- [Getting Started Guide](https://developers.llamaindex.ai/python/cloud/)
- [Full API Reference](https://developers.api.llamaindex.ai/api/python)

## Installation

```sh
pip install llama_cloud
```

## Quick Start

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)

# Parse a document
job = client.parsing.create(
    tier="agentic",
    version="latest",
    file_id="your-file-id",
)

print(job.id)
```

## File Uploads

```python
from pathlib import Path
from llama_cloud import LlamaCloud

client = LlamaCloud()

# Upload using a Path
client.files.create(
    file=Path("/path/to/document.pdf"),
    purpose="parse",
)

# Or using bytes with a tuple of (filename, contents, media_type)
client.files.create(
    file=("document.txt", b"content", "text/plain"),
    purpose="parse",
)
```

## Async Usage

```python
import asyncio
from llama_cloud import AsyncLlamaCloud

client = AsyncLlamaCloud()


async def main():
    job = await client.parsing.create(
        tier="agentic",
        version="latest",
        file_id="your-file-id",
    )
    print(job.id)


asyncio.run(main())
```

## MCP Server

Use the Llama Cloud MCP Server to enable AI assistants to interact with the API:

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=%40llamaindex%2Fllama-cloud-mcp&config=eyJuYW1lIjoiQGxsYW1haW5kZXgvbGxhbWEtY2xvdWQtbWNwIiwidHJhbnNwb3J0IjoiaHR0cCIsInVybCI6Imh0dHBzOi8vbGxhbWFjbG91ZC1wcm9kLnN0bG1jcC5jb20iLCJoZWFkZXJzIjp7IngtbGxhbWEtY2xvdWQtYXBpLWtleSI6Ik15IEFQSSBLZXkifX0)
[![Install in VS Code](https://img.shields.io/badge/_-Add_to_VS_Code-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PHBhdGggZmlsbD0iI0VFRSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMzAuMjM1IDM5Ljg4NGEyLjQ5MSAyLjQ5MSAwIDAgMS0xLjc4MS0uNzNMMTIuNyAyNC43OGwtMy40NiAyLjYyNC0zLjQwNiAyLjU4MmExLjY2NSAxLjY2NSAwIDAgMS0xLjA4Mi4zMzggMS42NjQgMS42NjQgMCAwIDEtMS4wNDYtLjQzMWwtMi4yLTJhMS42NjYgMS42NjYgMCAwIDEgMC0yLjQ2M0w3LjQ1OCAyMCA0LjY3IDE3LjQ1MyAxLjUwNyAxNC41N2ExLjY2NSAxLjY2NSAwIDAgMSAwLTIuNDYzbDIuMi0yYTEuNjY1IDEuNjY1IDAgMCAxIDIuMTMtLjA5N2w2Ljg2MyA1LjIwOUwyOC40NTIuODQ0YTIuNDg4IDIuNDg4IDAgMCAxIDEuODQxLS43MjljLjM1MS4wMDkuNjk5LjA5MSAxLjAxOS4yNDVsOC4yMzYgMy45NjFhMi41IDIuNSAwIDAgMSAxLjQxNSAyLjI1M3YuMDk5LS4wNDVWMzMuMzd2LS4wNDUuMDk1YTIuNTAxIDIuNTAxIDAgMCAxLTEuNDE2IDIuMjU3bC04LjIzNSAzLjk2MWEyLjQ5MiAyLjQ5MiAwIDAgMS0xLjA3Ny4yNDZabS43MTYtMjguOTQ3LTExLjk0OCA5LjA2MiAxMS45NTIgOS4wNjUtLjAwNC0xOC4xMjdaIi8+PC9zdmc+)](https://vscode.stainless.com/mcp/%7B%22name%22%3A%22%40llamaindex%2Fllama-cloud-mcp%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fllamacloud-prod.stlmcp.com%22%2C%22headers%22%3A%7B%22x-llama-cloud-api-key%22%3A%22My%20API%20Key%22%7D%7D)

## Error Handling

When the API returns a non-success status code, an `APIError` subclass is raised:

```python
import llama_cloud
from llama_cloud import LlamaCloud

client = LlamaCloud()

try:
    client.pipelines.list(project_id="my-project-id")
except llama_cloud.APIError as e:
    print(e.status_code)  # 400
    print(e.__class__.__name__)  # BadRequestError
```

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

## Retries and Timeouts

The SDK automatically retries requests 2 times on connection errors, timeouts, rate limits, and 5xx errors. Requests timeout after 1 minute by default. Functions that combine multiple API calls (e.g. `client.parsing.parse()`) will have larger timeouts by default to account for the multiple requests and polling.

```python
client = LlamaCloud(
    max_retries=0,  # Disable retries (default: 2)
    timeout=30.0,  # 30 second timeout (default: 1 minute)
)
```

## Pagination

List methods support auto-pagination with `for` loops:

```python
for run in client.extraction.runs.list(
    extraction_agent_id="agent-id",
    limit=20,
):
    print(run)
```

Or fetch one page at a time:

```python
page = client.extraction.runs.list(extraction_agent_id="agent-id", limit=20)
for run in page.items:
    print(run)

while page.has_next_page():
    page = page.get_next_page()
```

## Logging

Configure logging via the `LLAMA_CLOUD_LOG` environment variable or the `log` option:

```python
client = LlamaCloud(
    log="debug",  # "debug" | "info" | "warn" | "error" | "off"
)
```

## Requirements

- Python 3.9+

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
