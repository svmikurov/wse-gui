"""WSE application."""

import logging

import toga

from wse.core.auth.service import AuthService
from wse.core.navigation.navigation_id import NavigationID
from wse.di_container import AppContainer
from wse.interface.icore import INavigator

logger = logging.getLogger(__name__)


class WSE(toga.App):
    """WSE application."""

    _auth_service: AuthService
    _container: AppContainer
    _navigator: INavigator

    def startup(self) -> None:
        """Construct and show the application."""
        # Models

        # Application start with Main pages box content.
        self.main_window = toga.MainWindow(
            title=self.formal_name,
            size=toga.Size(440, 700),
        )
        self.main_window.show()

        # Set application dependencies
        container = AppContainer()
        self._auth_service = container.auth_service()
        navigator = self._set_navigator(container)

        # Set authentication status
        self._auth_service.is_authenticated()

        # Application start with Home page.
        navigator.navigate(NavigationID.HOME)

    def _set_navigator(self, container: AppContainer) -> INavigator:
        navigator = container.navigator()
        navigator.set_main_window(self.main_window)
        navigator.routes = container.routes()
        return navigator

    def on_exit(self) -> bool:
        """Call when the application closes."""
        self._auth_service.close()
        return True


def main() -> WSE:
    """Return the app instance."""
    return WSE()
