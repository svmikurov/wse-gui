"""Entry point for starting the application."""

import logging
from typing import Optional

from wse.app import WSE
from wse.container import ApplicationContainer
from wse.core.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def main() -> Optional[WSE]:
    """Create and return the application instance."""
    try:
        container = ApplicationContainer()
        app = container.app()
        logger.info('Application started successfully.')
        return app

    except Exception as e:
        # Logging exceptions to tracing stack.
        logger.error(f'Failed to start application: {e}', exc_info=True)
        return None
