# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud._utils import parse_datetime
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from llama_cloud.types.beta.directories import (
    FileAddResponse,
    FileGetResponse,
    FileListResponse,
    FileUpdateResponse,
    FileUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            metadata={"foo": "string"},
            target_directory_id="target_directory_id",
            unique_id="x",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        response = client.beta.directories.files.with_raw_response.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with client.beta.directories.files.with_streaming_response.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            client.beta.directories.files.with_raw_response.update(
                directory_file_id="directory_file_id",
                directory_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_file_id` but received ''"):
            client.beta.directories.files.with_raw_response.update(
                directory_file_id="",
                directory_id="directory_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.list(
            directory_id="directory_id",
        )
        assert_matches_type(SyncPaginatedCursor[FileListResponse], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.list(
            directory_id="directory_id",
            display_name="display_name",
            display_name_contains="display_name_contains",
            expand=["string", "string"],
            file_id="file_id",
            include_deleted=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            unique_id="unique_id",
            updated_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPaginatedCursor[FileListResponse], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.beta.directories.files.with_raw_response.list(
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncPaginatedCursor[FileListResponse], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.beta.directories.files.with_streaming_response.list(
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncPaginatedCursor[FileListResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            client.beta.directories.files.with_raw_response.list(
                directory_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.beta.directories.files.with_raw_response.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.beta.directories.files.with_streaming_response.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            client.beta.directories.files.with_raw_response.delete(
                directory_file_id="directory_file_id",
                directory_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_file_id` but received ''"):
            client.beta.directories.files.with_raw_response.delete(
                directory_file_id="",
                directory_id="directory_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.add(
            directory_id="directory_id",
            file_id="file_id",
        )
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.add(
            directory_id="directory_id",
            file_id="file_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            metadata={"foo": "string"},
            unique_id="unique_id",
        )
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: LlamaCloud) -> None:
        response = client.beta.directories.files.with_raw_response.add(
            directory_id="directory_id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: LlamaCloud) -> None:
        with client.beta.directories.files.with_streaming_response.add(
            directory_id="directory_id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileAddResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            client.beta.directories.files.with_raw_response.add(
                directory_id="",
                file_id="file_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )
        assert_matches_type(FileGetResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
            expand=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileGetResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.beta.directories.files.with_raw_response.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileGetResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.beta.directories.files.with_streaming_response.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileGetResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            client.beta.directories.files.with_raw_response.get(
                directory_file_id="directory_file_id",
                directory_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_file_id` but received ''"):
            client.beta.directories.files.with_raw_response.get(
                directory_file_id="",
                directory_id="directory_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.directories.files.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            external_file_id="external_file_id",
            metadata='{"source": "web", "priority": 1}',
            unique_id="unique_id",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: LlamaCloud) -> None:
        response = client.beta.directories.files.with_raw_response.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: LlamaCloud) -> None:
        with client.beta.directories.files.with_streaming_response.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            client.beta.directories.files.with_raw_response.upload(
                directory_id="",
                upload_file=b"Example data",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            metadata={"foo": "string"},
            target_directory_id="target_directory_id",
            unique_id="x",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.directories.files.with_raw_response.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.directories.files.with_streaming_response.update(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.update(
                directory_file_id="directory_file_id",
                directory_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_file_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.update(
                directory_file_id="",
                directory_id="directory_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.list(
            directory_id="directory_id",
        )
        assert_matches_type(AsyncPaginatedCursor[FileListResponse], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.list(
            directory_id="directory_id",
            display_name="display_name",
            display_name_contains="display_name_contains",
            expand=["string", "string"],
            file_id="file_id",
            include_deleted=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            unique_id="unique_id",
            updated_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPaginatedCursor[FileListResponse], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.directories.files.with_raw_response.list(
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[FileListResponse], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.directories.files.with_streaming_response.list(
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[FileListResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.list(
                directory_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.directories.files.with_raw_response.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.directories.files.with_streaming_response.delete(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.delete(
                directory_file_id="directory_file_id",
                directory_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_file_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.delete(
                directory_file_id="",
                directory_id="directory_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.add(
            directory_id="directory_id",
            file_id="file_id",
        )
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.add(
            directory_id="directory_id",
            file_id="file_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            metadata={"foo": "string"},
            unique_id="unique_id",
        )
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.directories.files.with_raw_response.add(
            directory_id="directory_id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileAddResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.directories.files.with_streaming_response.add(
            directory_id="directory_id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileAddResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.add(
                directory_id="",
                file_id="file_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )
        assert_matches_type(FileGetResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
            expand=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileGetResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.directories.files.with_raw_response.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileGetResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.directories.files.with_streaming_response.get(
            directory_file_id="directory_file_id",
            directory_id="directory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileGetResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.get(
                directory_file_id="directory_file_id",
                directory_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_file_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.get(
                directory_file_id="",
                directory_id="directory_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.directories.files.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            external_file_id="external_file_id",
            metadata='{"source": "web", "priority": 1}',
            unique_id="unique_id",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.directories.files.with_raw_response.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.directories.files.with_streaming_response.upload(
            directory_id="directory_id",
            upload_file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `directory_id` but received ''"):
            await async_client.beta.directories.files.with_raw_response.upload(
                directory_id="",
                upload_file=b"Example data",
            )
