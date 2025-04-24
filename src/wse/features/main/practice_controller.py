"""Defines home page controller."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.main import PracticeModel


@dataclass
class PracticeController(ContextController):
    """Practice page controller."""

    model: PracticeModel

    # Listener methods
    def request_data(self) -> None:
        """Request dat for info panel."""
        self.model.service_layer.get_response_data()
