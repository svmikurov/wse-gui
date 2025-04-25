"""Defines Swarm page controller."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from pprint import pprint
from typing import TYPE_CHECKING

import httpx
from toga.sources import Listener

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.figaro import SwarmModel, SwarmView

logger = logging.getLogger(__name__)


@dataclass
class SwarmController(ContextController, Listener):
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
        self.view.text_panel.change(text)