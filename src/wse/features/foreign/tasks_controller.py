"""Defines Foreign tasks page controller."""

from dataclasses import dataclass

from wse.features.shared.mvc import BaseController


@dataclass
class TasksController(BaseController):
    """Foreign tasks page controller."""
