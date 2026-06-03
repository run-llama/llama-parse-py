from __future__ import annotations

import os
import json
import asyncio
from typing import Any, Mapping

from llama_cloud import AsyncLlamaCloud
from llama_cloud._utils import lru_cache
from llama_cloud.types.beta.retrieval_retrieve_params import Rerank

MAX_POLLING_ATTEMPTS = 900
POLLING_INTERVAL = 2


def _get_status(metadata: Any) -> str:
    """Safely extract the `status` field from index/directory metadata."""
    if not metadata:
        return "unknown"
    if isinstance(metadata, Mapping):
        return str(metadata.get("status", "unknown"))  # type: ignore
    return str(getattr(metadata, "status", "unknown"))


@lru_cache(maxsize=1)
def get_client() -> AsyncLlamaCloud:
    return AsyncLlamaCloud(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY") or os.getenv("LLAMA_PARSE_API_KEY"),
        base_url=os.getenv("LLAMA_CLOUD_BASE_URL") or os.getenv("LLAMA_PARSE_BASE_URL"),
    )


@lru_cache(maxsize=1)
def get_project_id() -> str | None:
    return os.getenv("LLAMA_CLOUD_PROJECT_ID") or os.getenv("LLAMA_PARSE_PROJECT_ID")


async def create_index_from_directory() -> tuple[str, str]:
    client = get_client()
    directory = os.getenv("DATA_DIR", "data/")
    cloud_dir = await client.beta.directories.create(
        name=os.getenv("DIR_NAME", "index-v2-demo"),
        project_id=get_project_id(),
        description="Directory containing some data as a demo for Index V2 usage",
    )
    print(f"Created a directory on the LlamaParse platform with ID: {cloud_dir.id}")

    semaphore = asyncio.Semaphore(4)

    async def upload_file_to_dir(file: str) -> str:
        async with semaphore:
            fl_obj = await client.beta.directories.files.upload(
                directory_id=cloud_dir.id,
                upload_file=file,
                project_id=get_project_id(),
            )
            return fl_obj.id

    file_ids = await asyncio.gather(
        *[
            upload_file_to_dir(os.path.join(directory, f))
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
    )

    print(
        f"Uploaded {len(file_ids)} files in {directory} to the directory on the LlamaParse Platform, with the following IDs: {', '.join(file_ids)}"
    )

    idx = await client.beta.indexes.create(
        source_directory_id=cloud_dir.id, project_id=get_project_id(), name=os.getenv("INDEX_NAME", "index-v2-demo")
    )

    print(f"Created an index on the LlamaParse Platform with ID: {idx.id} and export config ID: {idx.export_config_id}")

    return idx.id, idx.export_config_id


async def sync_and_wait(index_id: str) -> None:
    client = get_client()

    await client.beta.indexes.sync(index_id=index_id)
    attempts = 0
    while attempts < MAX_POLLING_ATTEMPTS:
        idx = await client.beta.indexes.get(index_id=index_id)
        status = _get_status(idx.metadata)
        if status == "ready":
            return
        elif status == "failed":
            raise RuntimeError("Index sync failed")
        attempts += 1
        await asyncio.sleep(POLLING_INTERVAL)


async def retrieve(export_config_id: str) -> None:
    client = get_client()
    retrieved = await client.beta.retrieval.retrieve(
        index_id=export_config_id,
        query=os.getenv("INDEX_RETRIEVAL_QUERY", "What information is available for retrieval?"),
        top_k=10,
        score_threshold=0.5,
        rerank=Rerank(enabled=True, top_n=5),
    )
    for i, r in enumerate(retrieved.results):
        print(f"Retrieved chunk #{i + 1} (Score: {r.score or 'no score'})")
        print("Content:")
        print(r.content)
        print()
        if r.metadata is not None:
            print("Metadata")
            print(json.dumps(r.metadata, indent=2))
        print()
        print("#########################################")
        print()


async def run() -> None:
    index_id, export_config_id = await create_index_from_directory()
    await sync_and_wait(index_id)
    await retrieve(export_config_id)


def main() -> None:
    asyncio.run(run())
