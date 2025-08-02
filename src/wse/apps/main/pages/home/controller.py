"""Defines Home page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.features.base.mvc import BasePageController

from .interfaces import IHomeController, IHomeModel, IHomeView


@inject
@dataclass
class HomeController(
    BasePageController,
    IHomeController,
):
    """Home page controller."""

    _view: IHomeView
    _model: IHomeModel

    @override
    def _setup(self) -> None:
        self._model.add_observer(self)

    @override
    def on_open(self, **kwargs: object) -> None:
        """Call methods when page opens."""
        self._model.on_open()

    @override
    def user_authenticated(self) -> None:
        """Set content for authenticated user."""
        self._view.set_authenticated_content()

    @override
    def user_anonymous(self) -> None:
        """Set content for anonymous user."""
        self._view.set_anonymous_content()

    @override
    def logout(self) -> None:
        """Handle the logout event."""
        self._model.handle_logout()
