"""Defines Mathematical page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import ContextController


@dataclass
class MathematicalController(ContextController):
    """Mathematical page controller."""
