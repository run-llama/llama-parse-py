# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import ManagedIngestionStatusResponse
from llama_cloud.pagination import SyncPaginatedPipelineFiles, AsyncPaginatedPipelineFiles
from llama_cloud.types.pipelines import (
    PipelineFile,
    FileCreateResponse,
    FileGetStatusCountsResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.files.with_raw_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.files.with_streaming_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.files.with_raw_response.create(
                    pipeline_id="",
                    body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PipelineFile, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                custom_metadata={"foo": {"foo": "bar"}},
            )

        assert_matches_type(PipelineFile, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.files.with_raw_response.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(PipelineFile, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.files.with_streaming_response.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(PipelineFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.files.with_raw_response.update(
                    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.pipelines.files.with_raw_response.update(
                    file_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(SyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_name_contains="file_name_contains",
                limit=0,
                offset=0,
                only_manually_uploaded=True,
                order_by="order_by",
                statuses=["CANCELLED", "ERROR"],
            )

        assert_matches_type(SyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.files.with_raw_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.files.with_streaming_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(SyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.files.with_raw_response.list(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.files.with_raw_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.files.with_streaming_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.files.with_raw_response.delete(
                    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.pipelines.files.with_raw_response.delete(
                    file_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.get_status(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.files.with_raw_response.get_status(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.files.with_streaming_response.get_status(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.files.with_raw_response.get_status(
                    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.pipelines.files.with_raw_response.get_status(
                    file_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status_counts_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.pipelines.files.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                only_manually_uploaded=True,
            )

        assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.files.with_raw_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.files.with_streaming_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status_counts(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.files.with_raw_response.get_status_counts(
                    pipeline_id="",
                )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.files.with_raw_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.files.with_streaming_response.create(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.create(
                    pipeline_id="",
                    body=[{"file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PipelineFile, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                custom_metadata={"foo": {"foo": "bar"}},
            )

        assert_matches_type(PipelineFile, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.files.with_raw_response.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(PipelineFile, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.files.with_streaming_response.update(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(PipelineFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.update(
                    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.update(
                    file_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AsyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_name_contains="file_name_contains",
                limit=0,
                offset=0,
                only_manually_uploaded=True,
                order_by="order_by",
                statuses=["CANCELLED", "ERROR"],
            )

        assert_matches_type(AsyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.files.with_raw_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.files.with_streaming_response.list(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(AsyncPaginatedPipelineFiles[PipelineFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.list(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.files.with_raw_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.files.with_streaming_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.delete(
                    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.delete(
                    file_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.get_status(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.files.with_raw_response.get_status(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.files.with_streaming_response.get_status(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.get_status(
                    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.get_status(
                    file_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status_counts_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.pipelines.files.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                only_manually_uploaded=True,
            )

        assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.files.with_raw_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.files.with_streaming_response.get_status_counts(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(FileGetStatusCountsResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status_counts(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.files.with_raw_response.get_status_counts(
                    pipeline_id="",
                )
