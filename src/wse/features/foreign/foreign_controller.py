"""Defines Foreign page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import BaseController


@dataclass
class ForeignController(BaseController):
    """Foreign page controller."""
