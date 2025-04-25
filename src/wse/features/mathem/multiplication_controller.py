"""Defines Multiplication page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import ContextController


@dataclass
class MultiplicationController(ContextController):
    """Multiplication page controller."""
