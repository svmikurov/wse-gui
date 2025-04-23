"""Defines account page model."""

import logging

from wse.features.base.context import Context
from wse.features.base.mvc import BaseModel
from wse.interface.icore import IAuthService

logger = logging.getLogger(__name__)


class AccountModel(BaseModel):
    """Account page mode."""

    _context: Context

    def __init__(
        self,
        *args: object,
        auth_service: IAuthService,
        **kwargs: object,
    ) -> None:
        """Construct the model."""
        super().__init__(*args, **kwargs)
        self._auth_service = auth_service

    def render_context(self) -> None:
        """Render the context to view."""
        self._set_context()
        self._notify_render_context()

    def _set_context(self) -> None:
        self._context['is_authenticated'] = self._auth_service.check_auth()
        logger.debug(f'{self._context["is_authenticated"] = }')

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with auth context."""
        if self._context['is_authenticated'] is False:
            self._notify_render_auth_context()
        else:
            self._notify_render_not_auth_context()

    # Notifications
    def _notify_render_auth_context(self) -> None:
        """Notify controller to fill view with auth context."""
        self.subject.notify('render_auth_context')

    def _notify_render_not_auth_context(self) -> None:
        """Notify controller to fill view with auth context."""
        self.subject.notify('render_not_auth_context')
