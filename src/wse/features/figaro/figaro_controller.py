"""Defines Figaro page controller."""

from __future__ import annotations

from dataclasses import dataclass

from wse.features.base.mvc import ContextController


@dataclass
class FigaroController(ContextController):
    """Figaro page controller."""
