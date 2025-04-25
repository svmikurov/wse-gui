"""Defines home page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from toga.sources import Listener

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.main import PracticeModel, PracticeView

logger = logging.getLogger(__name__)


@dataclass
class PracticeController(ContextController, Listener):
    """Practice page controller."""

    model: PracticeModel
    view: PracticeView

    def __post_init__(self) -> None:
        """Subscribe to service layer."""
        super().__post_init__()
        self.model.service_layer.subject.add_listener(self)

    ####################################################################
    # Model listener methods

    def display_on_panel(self, text: str) -> None:
        """Display model data in a text panel."""
        text = self.model.get_text()
        self.view.text_panel.change(text)

    ####################################################################
    # View listener methods

    def request_data(self) -> None:
        """Request dat for info panel."""
        self.model.service_layer.request_text()
