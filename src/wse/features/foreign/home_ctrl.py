"""Defines Foreign home page controller."""

import logging
from dataclasses import dataclass

from wse.core.navigaion.navigator import navigator
from wse.features.shared.base import BaseController
from wse.features.shared.button_text import ButtonText

logger = logging.getLogger(__name__)


@dataclass
class ForeignCtrl(BaseController):
    """Foreign home page controller."""

    def navigate(self, button_text: ButtonText) -> None:
        """Navigate to page, the button event listener."""
        logger.debug(f'Pressed {button_text} button')
        navigator.navigate(button_text)
