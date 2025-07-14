"""WSE GUI application."""

import logging

import httpx
import toga
from injector import Injector

from .config.layout import StyleConfig
from .core.interfaces import INavigator, IRoutes
from .core.interfaces.iauth import IAuthService
from .di import create_injector
from .features.subapps.nav_id import NavID

logger = logging.getLogger(__name__)


class WSE(toga.App):  # type: ignore[misc]
    """WSE GUI application."""

    _injector: Injector
    _layout_config: StyleConfig
    _navigator: INavigator
    _start_page_id = NavID.HOME

    def startup(self) -> None:
        """Construct and show the Toga application."""
        self._set_injector()
        self._set_config()
        self._initialize_main_window()
        self._set_auth_status()
        self._set_navigator()
        self._navigate_to_start_page()

    def _initialize_main_window(self) -> None:
        main_window = self._injector.get(toga.MainWindow)

        # Configure the main window
        main_window.title = self.formal_name
        main_window.size = self._layout_config.window_size

        # Set and show main window
        self.main_window = main_window
        self.main_window.show()

    def _set_injector(self) -> None:
        """Set the `Injector` instance."""
        self._injector = create_injector()

    def _set_config(self) -> None:
        """Set application configuration."""
        self._layout_config = self._injector.get(StyleConfig)

    def _set_auth_status(self) -> None:
        """Set user authenticated status."""
        auth_service = self._injector.get(IAuthService)  # type: ignore[type-abstract]
        auth_service.set_auth_status()
        logger.info(f'User authenticated: {auth_service.is_auth}')

    def _set_navigator(self) -> None:
        """Set the page navigator."""
        self._navigator = self._injector.get(INavigator)  # type: ignore[type-abstract]
        routes = self._injector.get(IRoutes).routes  # type: ignore[type-abstract]

        # Configure navigator
        self._navigator.set_main_window(self.main_window)
        self._navigator.set_routes(routes)

    def _navigate_to_start_page(self) -> None:
        self._navigator.navigate(self._start_page_id)

    def on_exit(self) -> bool:
        """Call when the application closes."""
        self._injector.get(httpx.Client).close()
        return True


def main() -> WSE:
    """Return the app instance."""
    return WSE()
