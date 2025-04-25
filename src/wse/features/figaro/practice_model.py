"""Defines Practice page model."""
import json
import logging
from pathlib import Path

from wse.config.settings import PROJECT_PATH
from wse.features.base.mvc import BaseModel
from wse.features.main.containers.service_layer import ServiceLayer

logger = logging.getLogger(__name__)

TEXT_PATH: Path = PROJECT_PATH / 'temp' / 'api-response.txt'


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

    @property
    def text(self) -> str:
        """Get text as http response."""
        return TEXT_PATH.read_text()

    @staticmethod
    def format_json(text):
        return json.dumps(text, indent=4, ensure_ascii=False)

    def get_text(self) -> str:
        return self.format_json(self.text)

    def _set_context(self) -> None:
        """Set view context for render into view."""

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""
