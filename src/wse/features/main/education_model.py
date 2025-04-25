"""Defines Education page model."""

import logging

from wse.features.base.mvc import BaseModel

logger = logging.getLogger(__name__)


class EducationModel(BaseModel):
    """Education page model."""

    def _set_context(self) -> None:
        pass

    def _notify_render_context(self) -> None:
        """Temporary unused."""
