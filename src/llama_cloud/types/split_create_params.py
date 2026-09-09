# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .beta.split_category_param import SplitCategoryParam

__all__ = ["SplitCreateParams", "Configuration", "ConfigurationSplittingStrategy", "WebhookConfiguration"]


class SplitCreateParams(TypedDict, total=False):
    file_input: Required[str]
    """File ID or parse job ID"""

    organization_id: Optional[str]

    project_id: Optional[str]

    configuration: Optional[Configuration]
    """Split configuration with categories and splitting strategy."""

    configuration_id: Optional[str]
    """Saved configuration ID"""

    transaction_id: Optional[str]
    """Idempotency key scoped to the project.

    Reusing a key returns the original job; the new request body is ignored.
    """

    webhook_configuration_ids: Optional[SequenceNotStr[str]]
    """IDs of saved webhook configurations to notify for this job."""

    webhook_configurations: Optional[Iterable[WebhookConfiguration]]
    """Outbound webhook endpoints to notify on job status changes"""


class ConfigurationSplittingStrategy(TypedDict, total=False):
    """Strategy for splitting documents."""

    allow_uncategorized: Literal["forbid", "include", "omit"]
    """Controls handling of pages that don't match any category.

    'include': pages can be grouped as 'uncategorized' and included in results.
    'forbid': all pages must be assigned to a defined category. 'omit': pages can be
    classified as 'uncategorized' but are excluded from results.
    """


class Configuration(TypedDict, total=False):
    """Split configuration with categories and splitting strategy."""

    categories: Required[Iterable[SplitCategoryParam]]
    """Categories to split documents into."""

    splitting_strategy: ConfigurationSplittingStrategy
    """Strategy for splitting documents."""


class WebhookConfiguration(TypedDict, total=False):
    """Configuration for a single outbound webhook endpoint."""

    webhook_events: Optional[
        List[
            Literal[
                "batch.cancelled",
                "batch.error",
                "batch.pending",
                "batch.running",
                "batch.success",
                "classify.cancelled",
                "classify.error",
                "classify.partial_success",
                "classify.pending",
                "classify.running",
                "classify.success",
                "extract.cancelled",
                "extract.error",
                "extract.partial_success",
                "extract.pending",
                "extract.success",
                "parse.cancelled",
                "parse.error",
                "parse.partial_success",
                "parse.pending",
                "parse.running",
                "parse.success",
                "sheets.cancelled",
                "sheets.error",
                "sheets.partial_success",
                "sheets.pending",
                "sheets.success",
                "split.cancelled",
                "split.error",
                "split.pending",
                "split.processing",
                "split.success",
                "unmapped_event",
            ]
        ]
    ]
    """Events to subscribe to (e.g.

    'parse.success', 'extract.error'). If null, all events are delivered.
    """

    webhook_headers: Optional[Dict[str, str]]
    """Custom HTTP headers sent with each webhook request (e.g. auth tokens)"""

    webhook_output_format: Optional[str]
    """Response format sent to the webhook: 'string' (default) or 'json'"""

    webhook_signing_secret: Optional[str]
    """Shared signing secret used to sign webhook deliveries.

    When set, each request includes an HMAC-SHA256 signature of the request body in
    the 'LC-Signature' header (value 'sha256=<hex>'). Recompute the HMAC over the
    raw request body with this secret to verify the delivery is authentic.
    """

    webhook_url: Optional[str]
    """URL to receive webhook POST notifications"""
