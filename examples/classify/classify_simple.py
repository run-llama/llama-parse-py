import asyncio

from llama_cloud import AsyncLlamaCloud


async def classify_document() -> None:
    client = AsyncLlamaCloud()

    # Upload a file
    file_obj = await client.files.create(
        file="../example_files/attention_is_all_you_need.pdf",
        purpose="classify",
    )
    file_id = file_obj.id

    # Classify the document and wait for completion
    job = await client.classify.run(
        file_input=file_id,
        configuration={
            "rules": [
                {
                    "type": "ACADEMIC_PAPER",
                    "description": "Classify whether the document is an academic paper.",
                },
                {
                    "type": "OTHER",
                    "description": "Classify whether the document is from any other source besides academic papers.",
                },
            ],
            "mode": "FAST",
            "parsing_configuration": {
                "lang": "en",
                "max_pages": 5,
                # "target_pages": "1",  # Optional: specific pages to parse, cannot be used with max_pages
            },
        },
    )

    # Print the classification result
    result = job.result
    assert result is not None
    print(f"Classified type: {result.type}")
    print(f"Confidence: {result.confidence}")
    print(f"Reasoning: {result.reasoning}")


if __name__ == "__main__":
    asyncio.run(classify_document())
