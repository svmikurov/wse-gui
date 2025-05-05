"""WSE application."""

import logging

import toga

from wse.core.auth.service import AuthService
from wse.core.navigation.navigation_id import NavID
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

        # Application start with Home page.
        self._set_dependencies()
        self._navigator.navigate(NavID.HOME)

    def _set_dependencies(self) -> None:
        self._container = AppContainer()
        self._set_navigator()
        self._set_authentication_status()

    def _set_navigator(self) -> None:
        self._navigator = self._container.navigator()
        self._navigator.set_main_window(self.main_window)
        self._navigator.routes = self._container.routes()

    def _set_authentication_status(self) -> None:
        self._auth_service = self._container.auth_service()
        if not self._auth_service.is_authenticated():
            logger.info('User is not authenticated')

    def on_exit(self) -> bool:
        """Call when the application closes."""
        self._auth_service.close()
        return True


def main() -> WSE:
    """Return the app instance."""
    return WSE()
