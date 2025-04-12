"""Defines home page model."""

import logging

from wse.features.base.context import HomeContext
from wse.features.base.mvc import BaseModel
from wse.interface.ifeatures import ISubject

logger = logging.getLogger(__name__)


class User:
    """User model."""

    def __init__(self) -> None:
        """Construct the model."""
        self._name = None


class HomeModel(BaseModel):
    """Home page model."""

    def __init__(self, subject: ISubject) -> None:
        """Construct the model."""
        super().__init__(subject)
        self._user = User()
        self._context = HomeContext()

    def _set_context(self) -> None:
        logger.debug('Called `_set_context` method of `HomeModel`')

    def _notify_render_context(self) -> None:
        logger.debug('Called `_render_context` method of `HomeModel`')

        self.subject.notify('fill_info_panel', value=self.context.info_panel)
