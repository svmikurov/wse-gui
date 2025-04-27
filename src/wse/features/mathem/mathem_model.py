"""Defines Mathematical model."""

import logging

from toga.sources import Listener

from wse.features.base.mvc import BaseModel

logger = logging.getLogger(__name__)


class MathematicalModel(BaseModel, Listener):
    """Mathematical page model."""
