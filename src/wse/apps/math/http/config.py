"""Defines configuration for math app API."""

from pydantic import BaseModel


class MathAPIConfigV1(BaseModel):
    """Math app API configuration for v1 version."""

    base_url: str
    index: str
    calculation: dict[str, str]
