"""WSE application."""

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.di_container import AppContainer
from wse.interface.icore import IAuthService, INavigator


class WSE(toga.App):
    """WSE application."""

    _auth_service: IAuthService
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
