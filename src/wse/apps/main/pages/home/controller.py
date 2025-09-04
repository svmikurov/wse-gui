"""Home page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.feature.base.mvc import PageController

from .abc import HomeViewObserver
from .protocols import HomeModelProto, HomeViewProto


class _ViewObserver(HomeViewObserver):
    """Home page view notification observer."""

    _model: HomeModelProto

    @override
    def logout(self) -> None:
        """Handle the logout event."""
        self._model.logout()


@inject
@dataclass
class HomeController(
    PageController[HomeModelProto, HomeViewProto, None],
    _ViewObserver,
):
    """Home page controller."""

    _model: HomeModelProto
    _view: HomeViewProto

    def on_open(self, data: None = None) -> None:
        """Call methods when page opens."""
        self._model.check_auth_status()
