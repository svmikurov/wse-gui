"""Defines Foreign tasks page controller."""

from dataclasses import dataclass

from wse.features.shared.base_mvc import BaseController


@dataclass
class TasksController(BaseController):
    """Foreign tasks page controller."""
