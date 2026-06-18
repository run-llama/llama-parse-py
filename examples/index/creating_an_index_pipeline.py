# Index/sheets helpers intentionally use the deprecated v1 pipelines / beta.sheets API;
# migration to the indexes/retrievers + top-level sheets API is tracked separately.
# pyright: reportDeprecated=false
import asyncio

from llama_cloud import AsyncLlamaCloud
from llama_cloud.types.data_sink_create_params import Component
from llama_cloud.types.data_source_create_params import Component as DataSourceComponent
from llama_cloud.types.shared_params.cloud_s3_data_source import CloudS3DataSource
from llama_cloud.types.shared_params.cloud_pinecone_vector_store import CloudPineconeVectorStore


async def create_index() -> None:
    client = AsyncLlamaCloud()

    # Creating an index involves 5 main pieces
    # 1. The data sink (if blank, the default managed vector store will be used)
    # 2. The embedding configuration (if blank, the default embedding config will be used)
    # 3. The data source (if blank, no data will be connected by default, you can always add data later)
    # 4. The parsing parameters when ingesting data (if blank, the default parsing parameters will be used)
    # 5. The transform configuration when processing ingested data (if blank, the default transform configuration will be used)
    pipeline = await client.pipelines.upsert(
        name="my-first-index",
        project_id="my-project-id",
        data_sink_id=await create_data_sink(),  # optional
        embedding_config={
            "component": {
                "api_key": "sk-1234",
                "model_name": "text-embedding-3-small",
            },
            "type": "OPENAI_EMBEDDING",
        },
        llama_parse_parameters={"parse_mode": "parse_document_with_agent", "model": "openai-gpt-4-1-mini"},
        transform_config={"mode": "auto", "chunk_overlap": 128, "chunk_size": 1028},
    )

    print(pipeline.id)

    # Optional: Upload data after creating the index
    documents = await client.pipelines.documents.create(
        pipeline_id=pipeline.id,
        body=[
            {
                "text": "This is my first document to be indexed.",
                "metadata": {"source": "generated"},
            }
        ],
    )
    print(f"Uploaded {len(documents)} documents to the index.")

    # Optional: OR attach a data source after creating the index
    # data_source_id = await create_data_source()
    # await client.pipelines.data_sources.update_data_sources(
    #     pipeline_id=pipeline.id,
    #     body=[
    #         {
    #             "data_source_id": data_source_id,
    #             "sync_interval": 43200.0 # Optional, scheduled sync frequency in seconds. In this case, every 12 hours.
    #         },
    #     ]
    # )

    # Optional: Wait for indexing to complete
    status_resp = await client.pipelines.get_status(pipeline_id=pipeline.id)
    while status_resp.status not in ("NOT_STARTED", "IN_PROGRESS"):
        await asyncio.sleep(5)
        status_resp = await client.pipelines.get_status(pipeline_id=pipeline.id)

    print(f"Indexing completed with status: {status_resp.status}")


async def create_data_sink() -> str:
    client = AsyncLlamaCloud()

    # create a data source
    component: Component = CloudPineconeVectorStore(
        api_key="my-pinecone-api-key",
        index_name="my-pinecone-index",
    )
    data_sink = await client.data_sinks.create(
        name="my-pinecone-data-sink",
        component=component,
        sink_type="PINECONE",
    )

    return data_sink.id


async def create_data_source() -> str:
    client = AsyncLlamaCloud()

    # create a data source
    component: DataSourceComponent = CloudS3DataSource(
        bucket="my-bucket",
        aws_access_id="my-access-id",
        prefix="documents/",
    )
    data_source = await client.data_sources.create(
        name="my-s3-data-source",
        component=component,
        source_type="S3",
        project_id="my-project-id",
    )

    return data_source.id


if __name__ == "__main__":
    asyncio.run(create_index())
