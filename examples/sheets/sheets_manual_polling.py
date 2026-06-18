# Index/sheets helpers intentionally use the deprecated v1 pipelines / beta.sheets API;
# migration to the indexes/retrievers + top-level sheets API is tracked separately.
# pyright: reportDeprecated=false
import asyncio

import httpx

from llama_cloud import AsyncLlamaCloud
from llama_cloud.types.beta import SheetsParsingConfigParam


async def extract_tables() -> None:
    client = AsyncLlamaCloud()

    # Upload a spreadsheet
    file_obj = await client.files.create(file="../example_files/sample_spreadsheet.xlsx", purpose="parse")
    file_id = file_obj.id

    # Extract tables from the spreadsheet
    job = await client.beta.sheets.create(
        file_id=file_id,
        config=SheetsParsingConfigParam(
            generate_additional_metadata=True,
        ),
    )

    while True:
        result = await client.beta.sheets.get(spreadsheet_job_id=job.id, include_results=True)
        if result.status != "PENDING":
            break
        print(f"Job status: {result.status}. Waiting...")
        await asyncio.sleep(3)

    # Print extracted regions
    print(result.regions)

    # Download result parquet files
    assert result.regions is not None
    for region in result.regions:
        assert region.region_id is not None
        parquet_region_resp = await client.beta.sheets.get_result_table(
            region_type=region.region_type,  # type: ignore
            spreadsheet_job_id=result.id,
            region_id=region.region_id,
        )

        url = parquet_region_resp.url
        async with httpx.AsyncClient() as httpx_client:
            resp = await httpx_client.get(url)
            with open(f"./downloaded_region_{region.region_id}.parquet", "wb") as f:
                f.write(resp.content)
            print(f"Downloaded parquet for region {region.region_id}")

        parquet_metadata_resp = await client.beta.sheets.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id=result.id,
            region_id=region.region_id,
        )

        url = parquet_metadata_resp.url
        async with httpx.AsyncClient() as httpx_client:
            resp = await httpx_client.get(url)
            with open(f"./downloaded_region_{region.region_id}_metadata.parquet", "wb") as f:
                f.write(resp.content)
            print(f"Downloaded parquet metadata for region {region.region_id}")


if __name__ == "__main__":
    asyncio.run(extract_tables())
