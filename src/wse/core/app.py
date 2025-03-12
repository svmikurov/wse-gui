"""Defines the main application class."""

import asyncio

import toga

from wse.core.auth.auth import AuthService
from wse.config.config import Settings
from wse.core.logger import setup_logger
from wse.core.navigation.navigator import Navigator
from wse.core.navigation.routes import Routes

logger = setup_logger('app')


class WSE(toga.App):
    """Represents the WSE application."""

    def __init__(
        self,
        settings: Settings,
        auth_service: AuthService,
        navigator: Navigator,
    ) -> None:
        """Construct the application."""
        super().__init__(
            app_id=settings.APP_ID,
            app_name=settings.APP_NAME,
            formal_name=settings.APP_NAME,
        )
        self.settings = settings
        self.auth_service = auth_service
        self.navigator = navigator

    def startup(self) -> None:
        """Initialize and display the application window."""
        self.main_window = toga.MainWindow(
            size=toga.Size(*self.settings.screen_config.SCREEN_SIZE),
        )
        self.navigator.set_main_window(self.main_window)
        self.main_window.show()

        asyncio.create_task(self._check_authentication())

    async def _check_authentication(self) -> None:
        """Check authentication status and navigate accordingly."""
        if (
            not self.settings.AUTH_REQUIRED
            or await self.auth_service.is_authenticated()
        ):
            logger.info('User is authenticated, showing Home screen')
            self.navigator.navigate(Routes.HOME)
        else:
            logger.info('User is not authenticated, showing Login screen')
            self.navigator.navigate(Routes.LOGIN)
