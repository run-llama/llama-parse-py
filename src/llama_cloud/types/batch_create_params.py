# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BatchCreateParams", "Config", "ConfigJob"]


class BatchCreateParams(TypedDict, total=False):
    config: Required[Config]
    """Batch configuration snapshot to apply to this source directory."""

    source_directory_id: Required[str]
    """Directory whose files should be processed."""

    organization_id: Optional[str]

    project_id: Optional[str]


class ConfigJob(TypedDict, total=False):
    """Job to create for each file in the source directory."""

    configuration_id: Required[str]
    """Product configuration ID or built-in preset ID matching the job type."""

    type: Required[Literal["parse_v2", "extract_v2"]]
    """Product job type to run for each source directory file."""


class Config(TypedDict, total=False):
    """Batch configuration snapshot to apply to this source directory."""

    job: Required[ConfigJob]
    """Job to create for each file in the source directory."""
