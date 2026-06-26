import asyncio
from pathlib import Path
from datetime import datetime, timezone, timedelta

from llama_cloud import AsyncLlamaCloud

# Run a Parse V2 batch over every file in a directory:
#   1. create an ephemeral source directory
#   2. upload files into it
#   3. create a batch that runs parse_v2 on each file
#   4. poll until the batch reaches a terminal state
#   5. expand per-file results to resolve each file's parse job reference
#
# Batch creation requires a Pro or Enterprise plan and is rate limited.
# The client reads your API key from the LLAMA_CLOUD_API_KEY environment variable.

# A built-in Parse preset. You can also pass a saved "cfg-..." configuration id,
# or an "extract_v2" configuration id with type "extract_v2".
CONFIGURATION_ID = "cfg-PARSE_AGENTIC"
FILES = ["../example_files/attention_is_all_you_need.pdf", "../example_files/sample_spreadsheet.xlsx"]
TERMINAL_STATUSES = {"COMPLETED", "FAILED", "CANCELLED"}


async def run_batch() -> None:
    client = AsyncLlamaCloud()

    # 1. Ephemeral directories are automatically eligible for cleanup.
    expires_at = (datetime.now(timezone.utc) + timedelta(days=2)).isoformat()
    directory = await client.beta.directories.create(
        name="batch-example",
        type="ephemeral",
        expires_at=expires_at,
    )
    print(f"Created directory {directory.id}")

    # 2. Upload the files to process.
    for file_path in FILES:
        path = Path(file_path)
        await client.beta.directories.files.upload(
            directory.id,
            upload_file=path,
            display_name=path.name,
        )
        print(f"Uploaded {path.name}")

    # 3. Create the batch. The same product job runs on every file.
    batch = await client.batches.create(
        source_directory_id=directory.id,
        config={"job": {"type": "parse_v2", "configuration_id": CONFIGURATION_ID}},
    )
    print(f"Created batch {batch.id} ({batch.status})")

    # 4. Poll until the batch reaches a terminal state.
    status = batch.status
    while status not in TERMINAL_STATUSES:
        await asyncio.sleep(10)
        status = (await client.batches.get(batch.id)).status
        print(f"Batch status: {status}")

    # Batch-level FAILED means the orchestration failed and cannot provide a
    # reliable per-file result set.
    if status == "FAILED":
        raise RuntimeError("Batch orchestration failed")

    # 5. Expand per-file results to resolve each file's parse job reference.
    #    Per-file failures are reported in `error_message`; successful files
    #    include a `job_reference` for the underlying parse job.
    completed = await client.batches.get(batch.id, expand=["results"])
    for result in completed.results or []:
        if result.error_message:
            print(f"{result.source_directory_file_id} failed: {result.error_message}")
        elif result.job_reference:
            print(f"{result.source_directory_file_id} -> {result.job_reference.type} {result.job_reference.id}")
        else:
            print(f"{result.source_directory_file_id} has no job reference yet")


if __name__ == "__main__":
    asyncio.run(run_batch())
