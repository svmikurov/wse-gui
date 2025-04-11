"""WSE application."""

import logging

import toga

from wse.constants import SCREEN_SIZE
from wse.core.navigation.navigation_id import NavigationID
from wse.di_container import AppContainer
from wse.interface.icore import IAuthService, INavigator
from wse.menu import MenuMixin
from wse.models.user import User
from wse.sources.text_panel_main import SourceMainPanel

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


class WSE(MenuMixin, toga.App):
    """WSE application."""

    user: User
    source_main_panel: SourceMainPanel
    _auth_service: IAuthService
    _container: AppContainer
    _navigator: INavigator

    def startup(self) -> None:
        """Construct and show the application."""
        # Models
        self.user = User()
        self.source_main_panel = SourceMainPanel(self.user)

        # Application start with Main pages box content.
        self.main_window = toga.MainWindow(
            title=self.formal_name,
            size=toga.Size(*SCREEN_SIZE),
        )
        self.main_window.show()

        # Application dependencies
        container = AppContainer()
        auth_service = container.auth_service()
        navigator = self._set_navigator(container)

        # Set authentication status
        auth_service.set_auth_status()

        # Application start with Home page.
        navigator.navigate(NavigationID.HOME)

    def _set_navigator(self, container: AppContainer) -> INavigator:
        navigator = container.navigator()
        navigator.set_main_window(self.main_window)
        navigator.routes = container.routes()
        return navigator


def main() -> WSE:
    """Return the app instance."""
    return WSE()
