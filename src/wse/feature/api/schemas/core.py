"""Core application data schemas."""

from ..schemas.base import BaseSchema


class InitialData(BaseSchema):
    """Application initial data schema."""

    balance: str
