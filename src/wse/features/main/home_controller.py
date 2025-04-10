"""Defines home page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import BaseContextController


@dataclass
class HomeController(BaseContextController):
    """Home page controller."""
