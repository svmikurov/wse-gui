"""Entry point for starting the application."""

import logging
from typing import Optional

from wse.core.app import WSE
from wse.core.di_container import DIContainer
from wse.core.logger import setup_logger

logger = setup_logger('main', level=logging.DEBUG)


def main() -> Optional[WSE]:
    """Create and return the application instance."""
    try:
        logger.info('Starting application')

        logger.debug('Initializing DI container...')
        container = DIContainer()

        logger.info(
            f'Application language is set to: {container.settings().LANGUAGE}'
        )

        logger.debug('Creating application instance...')
        app = container.app()

        logger.info('Application started successfully.')
        return app

    except Exception as e:
        # Logging exceptions to tracing stack.
        logger.error(f'Failed to start application: {e}', exc_info=True)
        return None
