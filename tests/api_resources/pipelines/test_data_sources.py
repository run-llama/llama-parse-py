# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import Pipeline, ManagedIngestionStatusResponse
from llama_cloud.types.pipelines import (
    PipelineDataSource,
    DataSourceGetDataSourcesResponse,
    DataSourceUpdateDataSourcesResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = client.pipelines.data_sources.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PipelineDataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = client.pipelines.data_sources.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                sync_interval=0,
            )

        assert_matches_type(PipelineDataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.data_sources.with_raw_response.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(PipelineDataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.data_sources.with_streaming_response.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = response.parse()
                assert_matches_type(PipelineDataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.update(
                    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.update(
                    data_source_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = client.pipelines.data_sources.get_data_sources(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(DataSourceGetDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.data_sources.with_raw_response.get_data_sources(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceGetDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.data_sources.with_streaming_response.get_data_sources(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = response.parse()
                assert_matches_type(DataSourceGetDataSourcesResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.get_data_sources(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = client.pipelines.data_sources.get_status(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.data_sources.with_raw_response.get_status(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.data_sources.with_streaming_response.get_status(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.get_status(
                    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.get_status(
                    data_source_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = client.pipelines.data_sources.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = client.pipelines.data_sources.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        assert_matches_type(Pipeline, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.data_sources.with_raw_response.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(Pipeline, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.data_sources.with_streaming_response.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = response.parse()
                assert_matches_type(Pipeline, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_sync(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.sync(
                    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.sync(
                    data_source_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = client.pipelines.data_sources.update_data_sources(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert_matches_type(DataSourceUpdateDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.data_sources.with_raw_response.update_data_sources(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceUpdateDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.data_sources.with_streaming_response.update_data_sources(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = response.parse()
                assert_matches_type(DataSourceUpdateDataSourcesResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_data_sources(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.data_sources.with_raw_response.update_data_sources(
                    pipeline_id="",
                    body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                )


class TestAsyncDataSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = await async_client.pipelines.data_sources.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PipelineDataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = await async_client.pipelines.data_sources.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                sync_interval=0,
            )

        assert_matches_type(PipelineDataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.data_sources.with_raw_response.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(PipelineDataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.data_sources.with_streaming_response.update(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = await response.parse()
                assert_matches_type(PipelineDataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.update(
                    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.update(
                    data_source_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = await async_client.pipelines.data_sources.get_data_sources(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(DataSourceGetDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.data_sources.with_raw_response.get_data_sources(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceGetDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.data_sources.with_streaming_response.get_data_sources(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = await response.parse()
                assert_matches_type(DataSourceGetDataSourcesResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.get_data_sources(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = await async_client.pipelines.data_sources.get_status(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.data_sources.with_raw_response.get_status(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.data_sources.with_streaming_response.get_status(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = await response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.get_status(
                    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.get_status(
                    data_source_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = await async_client.pipelines.data_sources.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = await async_client.pipelines.data_sources.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        assert_matches_type(Pipeline, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.data_sources.with_raw_response.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(Pipeline, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.data_sources.with_streaming_response.sync(
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = await response.parse()
                assert_matches_type(Pipeline, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.sync(
                    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    pipeline_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.sync(
                    data_source_id="",
                    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            data_source = await async_client.pipelines.data_sources.update_data_sources(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert_matches_type(DataSourceUpdateDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.data_sources.with_raw_response.update_data_sources(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceUpdateDataSourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.data_sources.with_streaming_response.update_data_sources(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                data_source = await response.parse()
                assert_matches_type(DataSourceUpdateDataSourcesResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_data_sources(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.data_sources.with_raw_response.update_data_sources(
                    pipeline_id="",
                    body=[{"data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                )
