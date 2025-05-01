"""Defines Multiplication page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.mathem import MultiplicationModel, MultiplicationView

logger = logging.getLogger(__name__)


@dataclass
class MultiplicationController(ContextController):
    """Multiplication page controller."""

    model: MultiplicationModel
    view: MultiplicationView

    def __post_init__(self):
        self.view.button_handler.subject.add_listener(self)