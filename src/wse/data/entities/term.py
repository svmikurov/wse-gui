"""Defines Term entity."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Term:
    """Term entity."""

    id: str
    name: str
    definition: str
    created_at: datetime


@dataclass(frozen=True)
class Terms:
    """Terms entity data."""

    count: int | None = None
    next_url: str | None = None
    previous_url: str | None = None
    terms: list[Term] | None = None
