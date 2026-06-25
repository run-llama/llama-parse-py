# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .classifier_rule_param import ClassifierRuleParam
from .classify_parsing_configuration_param import ClassifyParsingConfigurationParam

__all__ = ["JobCreateParams", "WebhookConfiguration"]


class JobCreateParams(TypedDict, total=False):
    file_ids: Required[SequenceNotStr[str]]
    """The IDs of the files to classify"""

    rules: Required[Iterable[ClassifierRuleParam]]
    """The rules to classify the files"""

    organization_id: Optional[str]

    project_id: Optional[str]

    mode: Literal["FAST", "MULTIMODAL"]
    """The classification mode to use"""

    parsing_configuration: ClassifyParsingConfigurationParam
    """The configuration for the parsing job"""

    webhook_configurations: Iterable[WebhookConfiguration]
    """List of webhook configurations for notifications"""


class WebhookConfiguration(TypedDict, total=False):
    """Webhook configuration for receiving parsing job notifications.

    Webhooks are called when specified events occur during job processing.
    Configure multiple webhook configurations to send to different endpoints.
    """

    webhook_events: Optional[SequenceNotStr[str]]
    """Events that trigger this webhook.

    Options: 'parse.success' (job completed), 'parse.error' (job failed),
    'parse.partial_success' (some pages failed), 'parse.pending', 'parse.running',
    'parse.cancelled'. If not specified, webhook fires for all events
    """

    webhook_headers: Optional[Dict[str, object]]
    """Custom HTTP headers to include in webhook requests.

    Use for authentication tokens or custom routing. Example: {'Authorization':
    'Bearer xyz'}
    """

    webhook_output_format: Optional[Literal["json", "string"]]
    """Format of the webhook payload body.

    'string' (default) sends the payload as a JSON-encoded string; 'json' sends it
    as a JSON object.
    """

    webhook_url: Optional[str]
    """HTTPS URL to receive webhook POST requests. Must be publicly accessible"""
