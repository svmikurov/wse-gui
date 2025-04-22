"""Defines account page model."""

import logging

from wse.features.base.mvc import BaseModel
from wse.interface.icore import IAuthService

logger = logging.getLogger(__name__)


class AccountModel(BaseModel):
    """Account page mode."""

    def __init__(
        self,
        *args: object,
        auth_service: IAuthService,
        **kwargs: object,
    ) -> None:
        """Construct the model."""
        super().__init__(*args, **kwargs)
        self._auth_service = auth_service

    def _set_context(self) -> None:
        self._context['is_authenticated'] = False

    def _notify_context_render(self) -> None:
        """Notify controller to fill view with auth context."""
        if self._context['is_authenticated'] is False:
            self._notify_auth_context_render()
        else:
            self._notify_not_auth_context_render()

    # Notifications
    def _notify_auth_context_render(self) -> None:
        """Notify controller to fill view with auth context."""
        self.subject.notify('render_auth_context')

    def _notify_not_auth_context_render(self) -> None:
        """Notify controller to fill view with auth context."""
        self.subject.notify('render_not_auth_context')
