"""Defines Swarm page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.figaro import SwarmModel, SwarmView

logger = logging.getLogger(__name__)


@dataclass
class SwarmController(ContextController):
    """Swarm page controller."""

    model: SwarmModel
    view: SwarmView

    ####################################################################
    # Model listener methods
    def handel_request(self, endpoint: str) -> None:
        """Perform http request by endpoint."""
        self.model.perform_request(endpoint)

    ####################################################################
    # View listener methods

    def display_data(self, text: str) -> None:
        """Display data into text panel."""
        self.view.text_panel.change(text)
