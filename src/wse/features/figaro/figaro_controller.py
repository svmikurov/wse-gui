"""Defines Figaro page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from toga.sources import Listener

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.figaro import FigaroModel, FigaroView

logger = logging.getLogger(__name__)


@dataclass
class FigaroController(ContextController, Listener):
    """Figaro page controller."""

    model: FigaroModel
    view: FigaroView

    ####################################################################
    # Model listener methods

    ####################################################################
    # View listener methods

    def request_data(self) -> None:
        """Request dat for info panel."""
