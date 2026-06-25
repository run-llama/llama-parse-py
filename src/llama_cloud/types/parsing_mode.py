# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ParsingMode"]

ParsingMode: TypeAlias = Literal[
    "parse_document_with_agent",
    "parse_document_with_llm",
    "parse_document_with_lvm",
    "parse_page_with_agent",
    "parse_page_with_layout_agent",
    "parse_page_with_llm",
    "parse_page_with_lvm",
    "parse_page_without_llm",
]
