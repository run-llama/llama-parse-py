# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.extract import (
    review_get_params,
    review_create_params,
    review_reject_params,
    review_reopen_params,
    review_approve_params,
    review_list_events_params,
    review_change_fields_params,
)
from ...types.extract.extract_review import ExtractReview
from ...types.extract.extract_review_event import ExtractReviewEvent

__all__ = ["ReviewResource", "AsyncReviewResource"]


class ReviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return ReviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return ReviewResourceWithStreamingResponse(self)

    def create(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        confidence_threshold: float | Omit = omit,
        fields_in_scope: SequenceNotStr[str] | Omit = omit,
        required_fields: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Turn review on for an extract job.

        Fields read below `confidence_threshold`, and required fields left empty, are
        flagged for a person to check. Every setting has a default, so the body can be
        left out. A job still running can be named: it waits for review once it
        completes. A job that failed or was cancelled without a review, or that cannot
        be reviewed, answers 409 with `code: job_not_reviewable`; a field in
        `fields_in_scope` the job's schema does not have answers 400.

        Answers 201 with the new review, or 200 with the job's existing review, whose
        settings stay as they are.

        Args:
          confidence_threshold: Fields read below this confidence are flagged.

          fields_in_scope: JSON Pointers of the fields the threshold applies to; empty means all.

          required_fields: JSON Pointers of fields flagged when empty; defaults to the schema's required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            path_template("/api/v2/extract/{job_id}/review", job_id=job_id),
            body=maybe_transform(
                {
                    "confidence_threshold": confidence_threshold,
                    "fields_in_scope": fields_in_scope,
                    "required_fields": required_fields,
                },
                review_create_params.ReviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_create_params.ReviewCreateParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    def approve(
        self,
        job_id: str,
        *,
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sign_off: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Approve the reviewed result.

        While flagged fields nobody checked remain, answers 409 with `code: open_flags`
        and their `paths`, unless `sign_off` confirms them as part of approving. A job
        that has not completed answers 409 with `code: job_not_reviewable`. A `revision`
        other than the review's latest answers 409 with `code: stale_revision` and the
        latest `revision`.

        Args:
          revision: The review's revision as the caller last read it.

          sign_off: Confirm the flagged fields nobody checked as part of approving.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            path_template("/api/v2/extract/{job_id}/review/approve", job_id=job_id),
            body=maybe_transform(
                {
                    "revision": revision,
                    "sign_off": sign_off,
                },
                review_approve_params.ReviewApproveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_approve_params.ReviewApproveParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    def change_fields(
        self,
        job_id: str,
        *,
        changes: Iterable[review_change_fields_params.Change],
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Confirm, correct, clear, restore or undo fields of a completed job.

        The changes apply in order, in one write. A job without a review gets one with
        the default settings, at revision 0. A path that is not a field of the job, or a
        value the field's schema refuses, answers 400 and changes nothing. A job that
        has not completed answers 409 with `code: job_not_reviewable`. A `revision`
        other than the review's latest answers 409 with `code: stale_revision` and the
        latest `revision`.

        Args:
          changes: Changes to apply, in order.

          revision: The review's revision as the caller last read it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            path_template("/api/v2/extract/{job_id}/review/fields", job_id=job_id),
            body=maybe_transform(
                {
                    "changes": changes,
                    "revision": revision,
                },
                review_change_fields_params.ReviewChangeFieldsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_change_fields_params.ReviewChangeFieldsParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    def get(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Get an extract job's review: its flags, field actions and decision, with the
        result as the model read it and as reviewed. A job without a review answers 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/api/v2/extract/{job_id}/review", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_get_params.ReviewGetParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    def list_events(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ExtractReviewEvent]:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        List a review's history, newest first.

        Args:
          page_size: Events per page.

          page_token: Token from the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get_api_list(
            path_template("/api/v2/extract/{job_id}/review/events", job_id=job_id),
            page=SyncPaginatedCursor[ExtractReviewEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    review_list_events_params.ReviewListEventsParams,
                ),
            ),
            model=ExtractReviewEvent,
        )

    def reject(
        self,
        job_id: str,
        *,
        reason: str,
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Reject the result, with a reason. A job that failed or was cancelled can be
        rejected, which closes a review turned on while it ran. A job still queued or
        running answers 409 with `code: job_not_reviewable`. A `revision` other than the
        review's latest answers 409 with `code: stale_revision` and the latest
        `revision`.

        Args:
          reason: Why the result was rejected.

          revision: The review's revision as the caller last read it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            path_template("/api/v2/extract/{job_id}/review/reject", job_id=job_id),
            body=maybe_transform(
                {
                    "reason": reason,
                    "revision": revision,
                },
                review_reject_params.ReviewRejectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_reject_params.ReviewRejectParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    def reopen(
        self,
        job_id: str,
        *,
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Put an approved or rejected review back to pending. Its field actions stay.

        A `revision` other than the review's latest answers 409 with
        `code: stale_revision` and the latest `revision`.

        Args:
          revision: The review's revision as the caller last read it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            path_template("/api/v2/extract/{job_id}/review/reopen", job_id=job_id),
            body=maybe_transform({"revision": revision}, review_reopen_params.ReviewReopenParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_reopen_params.ReviewReopenParams,
                ),
            ),
            cast_to=ExtractReview,
        )


class AsyncReviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncReviewResourceWithStreamingResponse(self)

    async def create(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        confidence_threshold: float | Omit = omit,
        fields_in_scope: SequenceNotStr[str] | Omit = omit,
        required_fields: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Turn review on for an extract job.

        Fields read below `confidence_threshold`, and required fields left empty, are
        flagged for a person to check. Every setting has a default, so the body can be
        left out. A job still running can be named: it waits for review once it
        completes. A job that failed or was cancelled without a review, or that cannot
        be reviewed, answers 409 with `code: job_not_reviewable`; a field in
        `fields_in_scope` the job's schema does not have answers 400.

        Answers 201 with the new review, or 200 with the job's existing review, whose
        settings stay as they are.

        Args:
          confidence_threshold: Fields read below this confidence are flagged.

          fields_in_scope: JSON Pointers of the fields the threshold applies to; empty means all.

          required_fields: JSON Pointers of fields flagged when empty; defaults to the schema's required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            path_template("/api/v2/extract/{job_id}/review", job_id=job_id),
            body=await async_maybe_transform(
                {
                    "confidence_threshold": confidence_threshold,
                    "fields_in_scope": fields_in_scope,
                    "required_fields": required_fields,
                },
                review_create_params.ReviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_create_params.ReviewCreateParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    async def approve(
        self,
        job_id: str,
        *,
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sign_off: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Approve the reviewed result.

        While flagged fields nobody checked remain, answers 409 with `code: open_flags`
        and their `paths`, unless `sign_off` confirms them as part of approving. A job
        that has not completed answers 409 with `code: job_not_reviewable`. A `revision`
        other than the review's latest answers 409 with `code: stale_revision` and the
        latest `revision`.

        Args:
          revision: The review's revision as the caller last read it.

          sign_off: Confirm the flagged fields nobody checked as part of approving.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            path_template("/api/v2/extract/{job_id}/review/approve", job_id=job_id),
            body=await async_maybe_transform(
                {
                    "revision": revision,
                    "sign_off": sign_off,
                },
                review_approve_params.ReviewApproveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_approve_params.ReviewApproveParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    async def change_fields(
        self,
        job_id: str,
        *,
        changes: Iterable[review_change_fields_params.Change],
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Confirm, correct, clear, restore or undo fields of a completed job.

        The changes apply in order, in one write. A job without a review gets one with
        the default settings, at revision 0. A path that is not a field of the job, or a
        value the field's schema refuses, answers 400 and changes nothing. A job that
        has not completed answers 409 with `code: job_not_reviewable`. A `revision`
        other than the review's latest answers 409 with `code: stale_revision` and the
        latest `revision`.

        Args:
          changes: Changes to apply, in order.

          revision: The review's revision as the caller last read it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            path_template("/api/v2/extract/{job_id}/review/fields", job_id=job_id),
            body=await async_maybe_transform(
                {
                    "changes": changes,
                    "revision": revision,
                },
                review_change_fields_params.ReviewChangeFieldsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_change_fields_params.ReviewChangeFieldsParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    async def get(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Get an extract job's review: its flags, field actions and decision, with the
        result as the model read it and as reviewed. A job without a review answers 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/api/v2/extract/{job_id}/review", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_get_params.ReviewGetParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    def list_events(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExtractReviewEvent, AsyncPaginatedCursor[ExtractReviewEvent]]:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        List a review's history, newest first.

        Args:
          page_size: Events per page.

          page_token: Token from the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get_api_list(
            path_template("/api/v2/extract/{job_id}/review/events", job_id=job_id),
            page=AsyncPaginatedCursor[ExtractReviewEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    review_list_events_params.ReviewListEventsParams,
                ),
            ),
            model=ExtractReviewEvent,
        )

    async def reject(
        self,
        job_id: str,
        *,
        reason: str,
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Reject the result, with a reason. A job that failed or was cancelled can be
        rejected, which closes a review turned on while it ran. A job still queued or
        running answers 409 with `code: job_not_reviewable`. A `revision` other than the
        review's latest answers 409 with `code: stale_revision` and the latest
        `revision`.

        Args:
          reason: Why the result was rejected.

          revision: The review's revision as the caller last read it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            path_template("/api/v2/extract/{job_id}/review/reject", job_id=job_id),
            body=await async_maybe_transform(
                {
                    "reason": reason,
                    "revision": revision,
                },
                review_reject_params.ReviewRejectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_reject_params.ReviewRejectParams,
                ),
            ),
            cast_to=ExtractReview,
        )

    async def reopen(
        self,
        job_id: str,
        *,
        revision: int,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractReview:
        """
        Beta: answers 403 until extract review is enabled for the caller and their
        organization.

        Put an approved or rejected review back to pending. Its field actions stay.

        A `revision` other than the review's latest answers 409 with
        `code: stale_revision` and the latest `revision`.

        Args:
          revision: The review's revision as the caller last read it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            path_template("/api/v2/extract/{job_id}/review/reopen", job_id=job_id),
            body=await async_maybe_transform({"revision": revision}, review_reopen_params.ReviewReopenParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    review_reopen_params.ReviewReopenParams,
                ),
            ),
            cast_to=ExtractReview,
        )


class ReviewResourceWithRawResponse:
    def __init__(self, review: ReviewResource) -> None:
        self._review = review

        self.create = to_raw_response_wrapper(
            review.create,
        )
        self.approve = to_raw_response_wrapper(
            review.approve,
        )
        self.change_fields = to_raw_response_wrapper(
            review.change_fields,
        )
        self.get = to_raw_response_wrapper(
            review.get,
        )
        self.list_events = to_raw_response_wrapper(
            review.list_events,
        )
        self.reject = to_raw_response_wrapper(
            review.reject,
        )
        self.reopen = to_raw_response_wrapper(
            review.reopen,
        )


class AsyncReviewResourceWithRawResponse:
    def __init__(self, review: AsyncReviewResource) -> None:
        self._review = review

        self.create = async_to_raw_response_wrapper(
            review.create,
        )
        self.approve = async_to_raw_response_wrapper(
            review.approve,
        )
        self.change_fields = async_to_raw_response_wrapper(
            review.change_fields,
        )
        self.get = async_to_raw_response_wrapper(
            review.get,
        )
        self.list_events = async_to_raw_response_wrapper(
            review.list_events,
        )
        self.reject = async_to_raw_response_wrapper(
            review.reject,
        )
        self.reopen = async_to_raw_response_wrapper(
            review.reopen,
        )


class ReviewResourceWithStreamingResponse:
    def __init__(self, review: ReviewResource) -> None:
        self._review = review

        self.create = to_streamed_response_wrapper(
            review.create,
        )
        self.approve = to_streamed_response_wrapper(
            review.approve,
        )
        self.change_fields = to_streamed_response_wrapper(
            review.change_fields,
        )
        self.get = to_streamed_response_wrapper(
            review.get,
        )
        self.list_events = to_streamed_response_wrapper(
            review.list_events,
        )
        self.reject = to_streamed_response_wrapper(
            review.reject,
        )
        self.reopen = to_streamed_response_wrapper(
            review.reopen,
        )


class AsyncReviewResourceWithStreamingResponse:
    def __init__(self, review: AsyncReviewResource) -> None:
        self._review = review

        self.create = async_to_streamed_response_wrapper(
            review.create,
        )
        self.approve = async_to_streamed_response_wrapper(
            review.approve,
        )
        self.change_fields = async_to_streamed_response_wrapper(
            review.change_fields,
        )
        self.get = async_to_streamed_response_wrapper(
            review.get,
        )
        self.list_events = async_to_streamed_response_wrapper(
            review.list_events,
        )
        self.reject = async_to_streamed_response_wrapper(
            review.reject,
        )
        self.reopen = async_to_streamed_response_wrapper(
            review.reopen,
        )
