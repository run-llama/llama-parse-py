# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import ManagedIngestionStatusResponse
from llama_cloud.pagination import SyncPaginatedCloudDocuments, AsyncPaginatedCloudDocuments
from llama_cloud.types.pipelines import (
    CloudDocument,
    DocumentCreateResponse,
    DocumentUpsertResponse,
    DocumentGetChunksResponse,
    DocumentGetStatusCountsResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.create(
                    pipeline_id="",
                    body=[
                        {
                            "metadata": {"foo": "bar"},
                            "text": "text",
                        }
                    ],
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(SyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                limit=0,
                only_api_data_source_documents=True,
                only_direct_upload=True,
                skip=0,
                status_refresh_policy="cached",
            )

        assert_matches_type(SyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(SyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.list(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.delete(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.delete(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.delete(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.delete(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                client.pipelines.documents.with_raw_response.delete(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.get(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(CloudDocument, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.get(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(CloudDocument, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.get(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(CloudDocument, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.get(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                client.pipelines.documents.with_raw_response.get(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_chunks(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.get_chunks(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(DocumentGetChunksResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_chunks(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.get_chunks(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetChunksResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_chunks(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.get_chunks(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(DocumentGetChunksResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_chunks(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.get_chunks(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                client.pipelines.documents.with_raw_response.get_chunks(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.get_status(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.get_status(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.get_status(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.get_status(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                client.pipelines.documents.with_raw_response.get_status(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status_counts_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                only_direct_upload=True,
            )

        assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.get_status_counts(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.sync(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.sync(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.sync(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.sync(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                client.pipelines.documents.with_raw_response.sync(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = client.pipelines.documents.upsert(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert_matches_type(DocumentUpsertResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.documents.with_raw_response.upsert(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentUpsertResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.documents.with_streaming_response.upsert(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = response.parse()
                assert_matches_type(DocumentUpsertResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.documents.with_raw_response.upsert(
                    pipeline_id="",
                    body=[
                        {
                            "metadata": {"foo": "bar"},
                            "text": "text",
                        }
                    ],
                )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.create(
                    pipeline_id="",
                    body=[
                        {
                            "metadata": {"foo": "bar"},
                            "text": "text",
                        }
                    ],
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AsyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                limit=0,
                only_api_data_source_documents=True,
                only_direct_upload=True,
                skip=0,
                status_refresh_policy="cached",
            )

        assert_matches_type(AsyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(AsyncPaginatedCloudDocuments[CloudDocument], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.list(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.delete(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.delete(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.delete(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.delete(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.delete(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.get(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(CloudDocument, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.get(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(CloudDocument, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.get(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(CloudDocument, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.get(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.get(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_chunks(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.get_chunks(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(DocumentGetChunksResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_chunks(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.get_chunks(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetChunksResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_chunks(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.get_chunks(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(DocumentGetChunksResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_chunks(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.get_chunks(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.get_chunks(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.get_status(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.get_status(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.get_status(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.get_status(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.get_status(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status_counts_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                only_direct_upload=True,
            )

        assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(DocumentGetStatusCountsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.get_status_counts(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.sync(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.sync(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.sync(
                document_id="document_id",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.sync(
                    document_id="document_id",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.sync(
                    document_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            document = await async_client.pipelines.documents.upsert(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert_matches_type(DocumentUpsertResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.documents.with_raw_response.upsert(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentUpsertResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.documents.with_streaming_response.upsert(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {
                        "metadata": {"foo": "bar"},
                        "text": "text",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                document = await response.parse()
                assert_matches_type(DocumentUpsertResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.documents.with_raw_response.upsert(
                    pipeline_id="",
                    body=[
                        {
                            "metadata": {"foo": "bar"},
                            "text": "text",
                        }
                    ],
                )
