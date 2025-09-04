"""Authentication page controller."""

from dataclasses import dataclass

from injector import inject

from wse.feature.base.mvc import PageController

from .abc import AuthViewObserver
from .protocols import AuthModelProto, AuthViewProto


class _ViewObserver(
    AuthViewObserver,
):
    """Auth page view notification observer."""

    _model: AuthModelProto

    def success_authentication(self) -> None:
        """Handle the success authentication event."""
        self._model.handle_success_authentication()


@inject
@dataclass
class AuthController(
    _ViewObserver,
    PageController[AuthModelProto, AuthViewProto, None],
):
    """Auth page controller."""

    _model: AuthModelProto
    _view: AuthViewProto
