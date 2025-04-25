"""Defines Education page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import ContextController


@dataclass
class EducationController(ContextController):
    """Education page controller."""
