# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..status_enum import StatusEnum
from .classifier_rule_param import ClassifierRuleParam
from .classify_parsing_configuration_param import ClassifyParsingConfigurationParam

__all__ = ["ClassifyJobParam"]


class ClassifyJobParam(TypedDict, total=False):
    """A classify job."""

    id: Required[str]
    """Unique identifier"""

    project_id: Required[str]
    """The ID of the project"""

    rules: Required[Iterable[ClassifierRuleParam]]
    """The rules to classify the files"""

    status: Required[StatusEnum]
    """The status of the classify job"""

    user_id: Required[str]
    """The ID of the user"""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Creation datetime"""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    error_message: Optional[str]
    """Error message for the latest job attempt, if any."""

    job_record_id: Optional[str]
    """The job record ID associated with this status, if any."""

    mode: Literal["FAST", "MULTIMODAL"]
    """The classification mode to use"""

    parsing_configuration: ClassifyParsingConfigurationParam
    """The configuration for the parsing job"""

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Update datetime"""
