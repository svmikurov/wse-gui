"""Defines Practice page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import Controller


@dataclass
class ExamplesController(Controller):
    """Examples page controller."""
