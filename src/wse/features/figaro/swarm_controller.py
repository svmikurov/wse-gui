"""Defines Swarm page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from toga.sources import Listener

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.main import SwarmModel, SwarmView

logger = logging.getLogger(__name__)


@dataclass
class SwarmController(ContextController, Listener):
    """Swarm page controller."""

    model: SwarmModel
    view: SwarmView

    ####################################################################
    # Model listener methods

    ####################################################################
    # View listener methods

    def request_data(self) -> None:
        """Request dat for info panel."""
