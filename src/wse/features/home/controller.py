"""Defines home page controller."""

import logging

from wse.core.navigaion.navigator import navigator
from wse.features.shared.base import BaseController
from wse.features.shared.button_text import ButtonText

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


class HomeController(BaseController):
    """Home page controller."""

    def navigate(self, button_text: ButtonText) -> None:
        """Navigate to page, the button event listener."""
        logger.debug(f'Pressed {button_text} button')
        navigator.navigate(button_text)
