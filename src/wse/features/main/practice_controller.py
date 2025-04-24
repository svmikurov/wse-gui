"""Defines home page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import ContextController


@dataclass
class PracticeController(ContextController):
    """Practice page controller."""
