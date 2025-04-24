"""Defines home page model."""

import logging

from wse.core.api.client import ApiClient
from wse.features.base.context import HomeContext
from wse.features.base.mvc import BaseModel
from wse.interface.ifeatures import ISubject

logger = logging.getLogger(__name__)


class HomeModel(BaseModel):
    """Home page model."""

    api_client: ApiClient
    _context: HomeContext
    _subject: ISubject

    def __init__(self, subject: ISubject, api_client: ApiClient) -> None:
        """Construct the model."""
        super().__init__(subject=subject, api_client=api_client)
        self._context = HomeContext()

    def _set_context(self) -> None:
        pass

    @property
    def context(self) -> HomeContext:
        """View context."""
        return self._context

    # Notifications
    def _notify_context_render(self) -> None:
        self.subject.notify('fill_info_panel', value=self.context.info_panel)

    def _notify_render_context(self) -> None:
        """Temporary unused."""
