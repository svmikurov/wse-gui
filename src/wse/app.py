"""WSE GUI application."""

import toga
from injector import Injector

from .config.layout import StyleConfig
from .core.interfaces import INavigator, IRoutes
from .di import create_injector
from .features.subapps.nav_id import NavID


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
        self._set_main_window()
        self._set_navigator()
        self._navigate_to_start_page()

    def _set_main_window(self) -> None:
        self.main_window = toga.MainWindow(
            title=self.formal_name,
            size=self._layout_config.window_size,
        )
        self.main_window.show()

    def _set_injector(self) -> None:
        """Set the `Injector` instance."""
        self._injector = create_injector()

    def _set_config(self) -> None:
        """Set application configuration."""
        self._layout_config = self._injector.get(StyleConfig)

    def _set_navigator(self) -> None:
        """Set the page navigator."""
        self._navigator = self._injector.get(INavigator)  # type: ignore[type-abstract]
        routes = self._injector.get(IRoutes).routes  # type: ignore[type-abstract]

        # Configure navigator
        self._navigator.set_main_window(self.main_window)
        self._navigator.set_routes(routes)

    def _navigate_to_start_page(self) -> None:
        self._navigator.navigate(self._start_page_id)


def main() -> WSE:
    """Return the app instance."""
    return WSE()
