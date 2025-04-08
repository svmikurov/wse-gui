"""Defines Foreign params page controller."""

from dataclasses import dataclass

from wse.features.shared.base_mvc import BaseController


@dataclass
class ParamsController(BaseController):
    """Foreign params page controller."""
