"""Defines Figaro page model."""

import logging

from wse.features.base.mvc import BaseModel

logger = logging.getLogger(__name__)


class FigaroModel(BaseModel):
    """Figaro base model."""

    def _set_context(self) -> None:
        """Set view context for render into view."""

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""
