"""Defines Authentication page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.features.base.mvc import BasePageController

from .interfaces import IAuthController, IAuthModel, IAuthView


@inject
@dataclass
class AuthController(
    BasePageController,
    IAuthController,
):
    """Authentication page controller."""

    _model: IAuthModel
    _view: IAuthView

    @override
    def _setup(self) -> None:
        self._model.add_observer(self)

    # Notifications from View

    @override
    def success_authentication(self) -> None:
        """Handle the success authentication event."""
        self._model.handle_success_authentication()

    # Notifications from Model

    @override
    def credential_clean(self) -> None:
        """Handle the credential clean."""
        self._view.clear_credential()
