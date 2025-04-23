"""Defines home page model."""

import logging

from wse.features.base.context import HomeContext
from wse.features.base.mvc import BaseModel
from wse.interface.ifeatures import ISubject

logger = logging.getLogger(__name__)


class HomeModel(BaseModel):
    """Home page model."""

    _context: HomeContext

    def __init__(self, subject: ISubject) -> None:
        """Construct the model."""
        super().__init__(subject)
        self._context = HomeContext()

    def _set_context(self) -> None:
        pass

    def _notify_context_render(self) -> None:
        self.subject.notify('fill_info_panel', value=self.context.info_panel)

    @property
    def context(self) -> HomeContext:
        """View context."""
        return self._context

    def _notify_render_context(self) -> None:
        """Temporary unused."""
