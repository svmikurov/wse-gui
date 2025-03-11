"""Entry point for starting the application."""

import logging
from typing import Optional

from wse.container import ApplicationContainer
from wse.core.app import WSE
from wse.core.logger import setup_logger

logger = setup_logger('main', level=logging.DEBUG)


def main() -> Optional[WSE]:
    """Create and return the application instance."""
    try:
        container = ApplicationContainer()
        logger.info(
            f'Application language is set to: '
            f'{container.core.settings().LANGUAGE}'
        )
        app = container.app()
        logger.info('Application started successfully.')
        return app

    except Exception as e:
        # Logging exceptions to tracing stack.
        logger.error(f'Failed to start application: {e}', exc_info=True)
        return None
