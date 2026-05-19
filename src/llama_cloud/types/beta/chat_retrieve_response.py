# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ChatRetrieveResponse",
    "Event",
    "EventThinkingDeltaEvent",
    "EventTextDeltaEvent",
    "EventThinkingEvent",
    "EventTextEvent",
    "EventToolCallEvent",
    "EventToolResultEvent",
    "EventToolResultEventImageAttachment",
    "EventStopEvent",
    "EventStopEventUsage",
    "EventUserInputEvent",
    "JobMetadata",
]


class EventThinkingDeltaEvent(BaseModel):
    content: str

    type: Optional[Literal["thinking_delta"]] = None


class EventTextDeltaEvent(BaseModel):
    content: str

    type: Optional[Literal["text_delta"]] = None


class EventThinkingEvent(BaseModel):
    content: str

    type: Optional[Literal["thinking"]] = None


class EventTextEvent(BaseModel):
    content: str

    type: Optional[Literal["text"]] = None


class EventToolCallEvent(BaseModel):
    arguments: Dict[str, object]

    call_id: str

    name: str

    type: Optional[Literal["tool_call"]] = None


class EventToolResultEventImageAttachment(BaseModel):
    """Coordinates for lazily resolving a page screenshot presigned URL."""

    attachment_name: str

    source_id: str


class EventToolResultEvent(BaseModel):
    call_id: str

    name: str

    result: object

    image_attachment: Optional[EventToolResultEventImageAttachment] = None
    """Coordinates for lazily resolving a page screenshot presigned URL."""

    type: Optional[Literal["tool_result"]] = None


class EventStopEventUsage(BaseModel):
    duration_ms: Optional[float] = None

    total_input_tokens: Optional[int] = None

    total_output_tokens: Optional[int] = None

    turns: Optional[int] = None


class EventStopEvent(BaseModel):
    error: Optional[str] = None

    is_error: bool

    usage: EventStopEventUsage

    type: Optional[Literal["stop"]] = None


class EventUserInputEvent(BaseModel):
    content: str

    type: Optional[Literal["user_input"]] = None


Event: TypeAlias = Annotated[
    Union[
        EventThinkingDeltaEvent,
        EventTextDeltaEvent,
        EventThinkingEvent,
        EventTextEvent,
        EventToolCallEvent,
        EventToolResultEvent,
        EventStopEvent,
        EventUserInputEvent,
    ],
    PropertyInfo(discriminator="type"),
]


class JobMetadata(BaseModel):
    """Token usage and status from the most recent run.

    Null if the session has not been run yet.
    """

    duration_ms: Optional[float] = None

    error: Optional[str] = None

    export_config_ids: Optional[List[str]] = None

    is_error: Optional[bool] = None

    total_input_tokens: Optional[int] = None

    total_output_tokens: Optional[int] = None

    turns: Optional[int] = None


class ChatRetrieveResponse(BaseModel):
    """Full chat session including its complete event history."""

    events: List[Event]
    """Ordered list of events that make up the conversation history."""

    last_updated_at: str
    """ISO-format timestamp showing when the session was last updated."""

    session_id: str
    """Unique session identifier."""

    generated_title: Optional[str] = None
    """Auto-generated title derived from the first user message."""

    index_ids: Optional[List[str]] = None
    """Indexes this session is bound to. Null on unbound sessions."""

    job_metadata: Optional[JobMetadata] = None
    """Token usage and status from the most recent run.

    Null if the session has not been run yet.
    """
