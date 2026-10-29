from __future__ import annotations

import os
from typing import Dict, List, Optional

import httpx
import pytest
from respx import MockRouter

from llama_cloud import LlamaCloud
from llama_cloud.types.pipeline import Pipeline

# `lib/index` imports llama-index-core, which fails to import on Python 3.9 (the
# version `scripts/test` runs under) with a TypeError rather than an ImportError,
# so this module skips there the same way `tests/test_index.py` is left out.
try:
    import llama_index.core  # noqa: F401  # pyright: ignore[reportUnusedImport]
except Exception as err:  # pragma: no cover - depends on the interpreter version
    pytest.skip(f"llama-index-core unavailable: {err}", allow_module_level=True)

from llama_cloud.lib.index.api_utils import resolve_project_and_pipeline  # noqa: E402

# The helper deliberately calls the deprecated v1 `pipelines.list` (see the note
# at the top of api_utils.py); pytest is configured to turn warnings into errors.
pytestmark = pytest.mark.filterwarnings("ignore::DeprecationWarning")

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

PROJECT: Dict[str, object] = {"id": "proj-1", "name": "demo", "organization_id": "org-1"}
EMBEDDING: Dict[str, object] = {"type": "MANAGED_OPENAI_EMBEDDING", "component": {}}


def list_item(pipeline_id: str, status: str, embedding_config: Optional[Dict[str, object]] = None) -> Dict[str, object]:
    return {
        "id": pipeline_id,
        "name": "docs",
        "project_id": "proj-1",
        "status": status,
        "embedding_config": embedding_config,
    }


def resolve_by_name(client: LlamaCloud, name: str) -> Pipeline:
    _, pipeline = resolve_project_and_pipeline(
        client, name=name, pipeline_id=None, project_name=None, project_id="proj-1", organization_id=None
    )
    return pipeline


@pytest.mark.respx(base_url=base_url)
def test_name_lookup_reads_the_live_pipeline_by_id(respx_mock: MockRouter, client: LlamaCloud) -> None:
    # The list returns slim items (embedding config may be null) and may include
    # a same-named pipeline that is still being deleted. The helper must skip the
    # deleting one and return the full Pipeline from the detail endpoint.
    listed: List[Dict[str, object]] = [list_item("old", "DELETING"), list_item("live", "CREATED")]
    respx_mock.get("/api/v1/projects/proj-1").mock(return_value=httpx.Response(200, json=PROJECT))
    respx_mock.get("/api/v1/pipelines").mock(return_value=httpx.Response(200, json=listed))
    detail = respx_mock.get("/api/v1/pipelines/live").mock(
        return_value=httpx.Response(
            200, json={"id": "live", "name": "docs", "project_id": "proj-1", "embedding_config": EMBEDDING}
        )
    )

    pipeline = resolve_by_name(client, "docs")

    assert isinstance(pipeline, Pipeline)
    assert pipeline.id == "live"
    assert detail.called


@pytest.mark.respx(base_url=base_url)
def test_name_lookup_reports_a_pipeline_deleted_after_listing_as_not_found(
    respx_mock: MockRouter, client: LlamaCloud
) -> None:
    respx_mock.get("/api/v1/projects/proj-1").mock(return_value=httpx.Response(200, json=PROJECT))
    respx_mock.get("/api/v1/pipelines").mock(
        return_value=httpx.Response(200, json=[list_item("gone", "CREATED", EMBEDDING)])
    )
    respx_mock.get("/api/v1/pipelines/gone").mock(return_value=httpx.Response(404, json={"detail": "Not found"}))

    with pytest.raises(ValueError, match="not found"):
        resolve_by_name(client, "docs")
