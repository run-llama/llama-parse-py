# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["HuggingFaceInferenceAPIEmbedding"]


class HuggingFaceInferenceAPIEmbedding(BaseModel):
    token: Union[str, bool, None] = None
    """Hugging Face token.

    Will default to the locally saved token. Pass token=False if you don’t want to
    send your token to the server.
    """

    class_name: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None
    """Additional cookies to send to the server."""

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    headers: Optional[Dict[str, str]] = None
    """Additional headers to send to the server.

    By default only the authorization and user-agent headers are sent. Values in
    this dictionary will override the default values.
    """

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """Hugging Face model name. If None, the task will be used."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    pooling: Optional[Literal["cls", "last", "mean"]] = None
    """Enum of possible pooling choices with pooling behaviors."""

    query_instruction: Optional[str] = None
    """Instruction to prepend during query embedding."""

    task: Optional[str] = None
    """
    Optional task to pick Hugging Face's recommended model, used when model_name is
    left as default of None.
    """

    text_instruction: Optional[str] = None
    """Instruction to prepend during text embedding."""

    timeout: Optional[float] = None
    """The maximum number of seconds to wait for a response from the server.

    Loading a new model in Inference API can take up to several minutes. Defaults to
    None, meaning it will loop until the server is available.
    """
