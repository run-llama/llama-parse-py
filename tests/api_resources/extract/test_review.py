# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from llama_cloud.types.extract import (
    ExtractReview,
    ExtractReviewEvent,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReview:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        review = client.extract.review.create(
            job_id="job_id",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        review = client.extract.review.create(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            confidence_threshold=0.8,
            fields_in_scope=["/total", "/vendor/name"],
            required_fields=["/vendor/name"],
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.extract.review.with_raw_response.create(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.extract.review.with_streaming_response.create(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.review.with_raw_response.create(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve(self, client: LlamaCloud) -> None:
        review = client.extract.review.approve(
            job_id="job_id",
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve_with_all_params(self, client: LlamaCloud) -> None:
        review = client.extract.review.approve(
            job_id="job_id",
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sign_off=True,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_approve(self, client: LlamaCloud) -> None:
        response = client.extract.review.with_raw_response.approve(
            job_id="job_id",
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_approve(self, client: LlamaCloud) -> None:
        with client.extract.review.with_streaming_response.approve(
            job_id="job_id",
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_approve(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.review.with_raw_response.approve(
                job_id="",
                revision=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_change_fields(self, client: LlamaCloud) -> None:
        review = client.extract.review.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                }
            ],
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_change_fields_with_all_params(self, client: LlamaCloud) -> None:
        review = client.extract.review.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                    "value": 1250.5,
                }
            ],
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_change_fields(self, client: LlamaCloud) -> None:
        response = client.extract.review.with_raw_response.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                }
            ],
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_change_fields(self, client: LlamaCloud) -> None:
        with client.extract.review.with_streaming_response.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                }
            ],
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_change_fields(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.review.with_raw_response.change_fields(
                job_id="",
                changes=[
                    {
                        "change": "correct",
                        "path": "/total",
                    }
                ],
                revision=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        review = client.extract.review.get(
            job_id="job_id",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        review = client.extract.review.get(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.extract.review.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.extract.review.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.review.with_raw_response.get(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: LlamaCloud) -> None:
        review = client.extract.review.list_events(
            job_id="job_id",
        )
        assert_matches_type(SyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: LlamaCloud) -> None:
        review = client.extract.review.list_events(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: LlamaCloud) -> None:
        response = client.extract.review.with_raw_response.list_events(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(SyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: LlamaCloud) -> None:
        with client.extract.review.with_streaming_response.list_events(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(SyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_events(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.review.with_raw_response.list_events(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reject(self, client: LlamaCloud) -> None:
        review = client.extract.review.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reject_with_all_params(self, client: LlamaCloud) -> None:
        review = client.extract.review.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reject(self, client: LlamaCloud) -> None:
        response = client.extract.review.with_raw_response.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reject(self, client: LlamaCloud) -> None:
        with client.extract.review.with_streaming_response.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reject(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.review.with_raw_response.reject(
                job_id="",
                reason="The invoice total does not match the line items.",
                revision=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reopen(self, client: LlamaCloud) -> None:
        review = client.extract.review.reopen(
            job_id="job_id",
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reopen_with_all_params(self, client: LlamaCloud) -> None:
        review = client.extract.review.reopen(
            job_id="job_id",
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reopen(self, client: LlamaCloud) -> None:
        response = client.extract.review.with_raw_response.reopen(
            job_id="job_id",
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reopen(self, client: LlamaCloud) -> None:
        with client.extract.review.with_streaming_response.reopen(
            job_id="job_id",
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reopen(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.review.with_raw_response.reopen(
                job_id="",
                revision=0,
            )


class TestAsyncReview:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.create(
            job_id="job_id",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.create(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            confidence_threshold=0.8,
            fields_in_scope=["/total", "/vendor/name"],
            required_fields=["/vendor/name"],
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.review.with_raw_response.create(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.review.with_streaming_response.create(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.review.with_raw_response.create(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.approve(
            job_id="job_id",
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.approve(
            job_id="job_id",
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sign_off=True,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.review.with_raw_response.approve(
            job_id="job_id",
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.review.with_streaming_response.approve(
            job_id="job_id",
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_approve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.review.with_raw_response.approve(
                job_id="",
                revision=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_change_fields(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                }
            ],
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_change_fields_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                    "value": 1250.5,
                }
            ],
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_change_fields(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.review.with_raw_response.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                }
            ],
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_change_fields(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.review.with_streaming_response.change_fields(
            job_id="job_id",
            changes=[
                {
                    "change": "correct",
                    "path": "/total",
                }
            ],
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_change_fields(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.review.with_raw_response.change_fields(
                job_id="",
                changes=[
                    {
                        "change": "correct",
                        "path": "/total",
                    }
                ],
                revision=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.get(
            job_id="job_id",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.get(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.review.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.review.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.review.with_raw_response.get(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.list_events(
            job_id="job_id",
        )
        assert_matches_type(AsyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.list_events(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.review.with_raw_response.list_events(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.review.with_streaming_response.list_events(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[ExtractReviewEvent], review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.review.with_raw_response.list_events(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reject(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reject_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reject(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.review.with_raw_response.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reject(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.review.with_streaming_response.reject(
            job_id="job_id",
            reason="The invoice total does not match the line items.",
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reject(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.review.with_raw_response.reject(
                job_id="",
                reason="The invoice total does not match the line items.",
                revision=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reopen(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.reopen(
            job_id="job_id",
            revision=0,
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reopen_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        review = await async_client.extract.review.reopen(
            job_id="job_id",
            revision=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reopen(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.review.with_raw_response.reopen(
            job_id="job_id",
            revision=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ExtractReview, review, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reopen(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.review.with_streaming_response.reopen(
            job_id="job_id",
            revision=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ExtractReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reopen(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.review.with_raw_response.reopen(
                job_id="",
                revision=0,
            )
