from __future__ import annotations

import os
import json
from typing import Dict

import httpx
import pytest
from respx import MockRouter

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from llama_cloud._polling import PollingError
from llama_cloud.types.extract_configuration_param import ExtractConfigurationParam

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

CONFIGURATION: ExtractConfigurationParam = {"data_schema": {"type": "object"}, "extraction_target": "per_doc"}


def job(status: str, error_message: str | None = None) -> Dict[str, object]:
    return {
        "id": "exj-1",
        "created_at": "2026-11-12T00:00:00Z",
        "updated_at": "2026-11-12T00:00:00Z",
        "file_input": "dfl-1",
        "project_id": "prj-1",
        "status": status,
        "error_message": error_message,
        "extract_result": {"vendor_name": "Acme"} if status == "COMPLETED" else None,
    }


@pytest.mark.respx(base_url=base_url)
def test_run_creates_the_job_and_polls_until_completed(respx_mock: MockRouter, client: LlamaCloud) -> None:
    create = respx_mock.post("/api/v2/extract").mock(return_value=httpx.Response(200, json=job("PENDING")))
    get = respx_mock.get("/api/v2/extract/exj-1").mock(
        side_effect=[
            httpx.Response(200, json=job("RUNNING")),
            httpx.Response(200, json=job("COMPLETED")),
        ]
    )

    result = client.extract.run(
        file_input="dfl-1",
        configuration=CONFIGURATION,
        webhook_configuration_ids=["whc-1"],
        polling_interval=0.0,
        max_interval=0.0,
    )

    assert json.loads(create.calls.last.request.content) == {
        "file_input": "dfl-1",
        "configuration": CONFIGURATION,
        "webhook_configuration_ids": ["whc-1"],
    }
    assert get.call_count == 2
    assert result.status == "COMPLETED"
    assert result.extract_result == {"vendor_name": "Acme"}


@pytest.mark.respx(base_url=base_url)
def test_run_raises_when_the_job_fails(respx_mock: MockRouter, client: LlamaCloud) -> None:
    respx_mock.post("/api/v2/extract").mock(return_value=httpx.Response(200, json=job("PENDING")))
    respx_mock.get("/api/v2/extract/exj-1").mock(return_value=httpx.Response(200, json=job("FAILED", "bad schema")))

    with pytest.raises(PollingError, match="bad schema"):
        client.extract.run(file_input="dfl-1", configuration=CONFIGURATION, polling_interval=0.0, max_interval=0.0)


@pytest.mark.respx(base_url=base_url)
async def test_async_run_creates_the_job_and_polls_until_completed(
    respx_mock: MockRouter, async_client: AsyncLlamaCloud
) -> None:
    respx_mock.post("/api/v2/extract").mock(return_value=httpx.Response(200, json=job("PENDING")))
    get = respx_mock.get("/api/v2/extract/exj-1").mock(
        side_effect=[
            httpx.Response(200, json=job("RUNNING")),
            httpx.Response(200, json=job("COMPLETED")),
        ]
    )

    result = await async_client.extract.run(
        file_input="dfl-1", configuration=CONFIGURATION, polling_interval=0.0, max_interval=0.0
    )

    assert get.call_count == 2
    assert result.status == "COMPLETED"
