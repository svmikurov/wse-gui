"""Defines the main application class."""

import toga

from wse.core.auth.auth import AuthService
from wse.core.config import Settings
from wse.core.logger import setup_logger
from wse.features.auth.view import LoginView
from wse.features.main.view import HomeView

logger = setup_logger('app')


class WSE(toga.App):
    """Represents the WSE application."""

    def __init__(
        self,
        settings: Settings,
        auth_service: AuthService,
    ) -> None:
        """Construct the application."""
        super().__init__(
            app_id=settings.APP_ID,
            app_name=settings.APP_NAME,
            formal_name=settings.APP_NAME,
        )
        self.settings = settings
        self.auth_service = auth_service

    def startup(self) -> None:
        """Initialize and display the application window."""
        self.main_window = toga.MainWindow(
            size=toga.Size(*self.settings.ui_config.SCREEN_SIZE),
        )

        if self.auth_service.is_authenticated():
            logger.info('User is authenticated, showing Home screen')
            self.main_window.content = HomeView()
        else:
            logger.info('User is not authenticated, showing Login screen')
            self.main_window.content = LoginView()

        self.main_window.show()
