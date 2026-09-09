# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookConfigUpdateParams"]


class WebhookConfigUpdateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

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
    """Updated event subscriptions."""

    webhook_headers: Optional[Dict[str, str]]
    """Updated headers."""

    webhook_output_format: Optional[Literal["json", "string"]]
    """Updated output format."""

    webhook_signing_secret: Optional[str]
    """Updated signing secret (write-only). Send to rotate the secret."""

    webhook_url: Optional[str]
    """Updated webhook URL."""
