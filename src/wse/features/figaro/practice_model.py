"""Defines Practice page model."""

import logging

from wse.features.base.mvc import BaseModel
from wse.features.main.containers.service_layer import ServiceLayer

logger = logging.getLogger(__name__)


class PracticeModel(BaseModel):
    """Practice base model."""

    def __init__(
        self,
        *args: object,
        service_layer: ServiceLayer | None = None,
        **kwargs: object,
    ) -> None:
        """Construct the model."""
        super().__init__(*args, **kwargs)
        self.service_layer = service_layer

    def _set_context(self) -> None:
        """Set view context for render into view."""

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""
