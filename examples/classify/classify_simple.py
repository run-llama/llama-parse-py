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

    # Upload and wait for completion
    result = await client.classifier.classify(
        file_ids=[file_id],
        rules=[
            {
                "type": "ACADEMIC_PAPER",
                "description": "Classify whether the document is an academic paper.",
            },
            {
                "type": "OTHER",
                "description": "Classify whether the document is from any other source besides academic papers.",
            },
        ],
        parsing_configuration={
            "lang": "en",
            "max_pages": 5,
            # "target_pages": [1],  # Optional: specify particular pages to parse, cannot be used with max_pages
        },
        mode="FAST",  # Specify classification mode: "FAST" or "MULTIMODAL"
    )

    # Print the classification results
    for item in result.items:
        assert item.result is not None
        print(f"Classified type: {item.result.type}")
        print(f"Confidence: {item.result.confidence}")
        print(f"Reasoning: {item.result.reasoning}")


if __name__ == "__main__":
    asyncio.run(classify_document())
