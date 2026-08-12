# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .webhook_config_response import WebhookConfigResponse

__all__ = ["WebhookConfigListResponse"]

WebhookConfigListResponse: TypeAlias = List[WebhookConfigResponse]
