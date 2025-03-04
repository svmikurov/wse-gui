"""WSE application."""

import toga

from wse.core.auth.auth import AuthService
from wse.core.config import Settings
from wse.features.main.view import HomeView


class WSE(toga.App):
    """WSE application."""

    def __init__(
        self,
        settings: Settings,
        auth_service: AuthService,
    ) -> None:
        """Construct the application."""
        super().__init__()
        self.settings = settings
        self.auth_service = auth_service

    def startup(self) -> None:
        """Construct and show the application."""
        self.main_window = toga.MainWindow(
            # size=toga.Size(*self.settings.screen.SCREEN_SIZE),
        )

        # if self.auth_service.is_authenticated():
        self.main_window.content = HomeView()
        # else:
        #     self.main_window = Routes.LOGIN

        self.main_window.show()
