# Llama Cloud Python SDK

[![PyPI version](https://img.shields.io/pypi/v/llama_cloud.svg?label=pypi%20(stable))](https://pypi.org/project/llama_cloud/)

The official Python SDK for [LlamaParse](https://cloud.llamaindex.ai) - the enterprise platform for agentic OCR and document processing.

With this SDK, create powerful workflows across many features:

## MCP Server

Use the Llama Cloud MCP Server to enable AI assistants to interact with this API, allowing them to explore endpoints, make test requests, and use documentation to help integrate this SDK into your application.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=%40llamaindex%2Fllama-cloud-mcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBsbGFtYWluZGV4L2xsYW1hLWNsb3VkLW1jcCJdLCJlbnYiOnsiTExBTUFfQ0xPVURfQVBJX0tFWSI6Ik15IEFQSSBLZXkifX0)
[![Install in VS Code](https://img.shields.io/badge/_-Add_to_VS_Code-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PHBhdGggZmlsbD0iI0VFRSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMzAuMjM1IDM5Ljg4NGEyLjQ5MSAyLjQ5MSAwIDAgMS0xLjc4MS0uNzNMMTIuNyAyNC43OGwtMy40NiAyLjYyNC0zLjQwNiAyLjU4MmExLjY2NSAxLjY2NSAwIDAgMS0xLjA4Mi4zMzggMS42NjQgMS42NjQgMCAwIDEtMS4wNDYtLjQzMWwtMi4yLTJhMS42NjYgMS42NjYgMCAwIDEgMC0yLjQ2M0w3LjQ1OCAyMCA0LjY3IDE3LjQ1MyAxLjUwNyAxNC41N2ExLjY2NSAxLjY2NSAwIDAgMSAwLTIuNDYzbDIuMi0yYTEuNjY1IDEuNjY1IDAgMCAxIDIuMTMtLjA5N2w2Ljg2MyA1LjIwOUwyOC40NTIuODQ0YTIuNDg4IDIuNDg4IDAgMCAxIDEuODQxLS43MjljLjM1MS4wMDkuNjk5LjA5MSAxLjAxOS4yNDVsOC4yMzYgMy45NjFhMi41IDIuNSAwIDAgMSAxLjQxNSAyLjI1M3YuMDk5LS4wNDVWMzMuMzd2LS4wNDUuMDk1YTIuNTAxIDIuNTAxIDAgMCAxLTEuNDE2IDIuMjU3bC04LjIzNSAzLjk2MWEyLjQ5MiAyLjQ5MiAwIDAgMS0xLjA3Ny4yNDZabS43MTYtMjguOTQ3LTExLjk0OCA5LjA2MiAxMS45NTIgOS4wNjUtLjAwNC0xOC4xMjdaIi8+PC9zdmc+)](https://vscode.stainless.com/mcp/%7B%22name%22%3A%22%40llamaindex%2Fllama-cloud-mcp%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40llamaindex%2Fllama-cloud-mcp%22%5D%2C%22env%22%3A%7B%22LLAMA_CLOUD_API_KEY%22%3A%22My%20API%20Key%22%7D%7D)

> Note: You may need to set environment variables in your MCP client.

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
    client.beta.indexes.list(
        project_id="my-project-id",
    )
except llama_cloud.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except llama_cloud.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except llama_cloud.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
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
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).beta.indexes.list(
    project_id="my-project-id",
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

# More granular control:
client = LlamaCloud(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).beta.indexes.list(
    project_id="my-project-id",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `LLAMA_CLOUD_LOG` to `info`.

```shell
$ export LLAMA_CLOUD_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from llama_cloud import LlamaCloud

client = LlamaCloud()
response = client.beta.indexes.with_raw_response.list(
    project_id="my-project-id",
)
print(response.headers.get('X-My-Header'))

index = response.parse()  # get the object that `beta.indexes.list()` would have returned
print(index.id)
```

These methods return an [`APIResponse`](https://github.com/run-llama/llama-parse-py/tree/main/src/llama_cloud/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/run-llama/llama-parse-py/tree/main/src/llama_cloud/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.beta.indexes.with_streaming_response.list(
    project_id="my-project-id",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from llama_cloud import LlamaCloud, DefaultHttpxClient

client = LlamaCloud(
    # Or use the `LLAMA_CLOUD_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from llama_cloud import LlamaCloud

with LlamaCloud() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/run-llama/llama-parse-py/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import llama_cloud
print(llama_cloud.__version__)
```

## Requirements

- Python 3.9+

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
