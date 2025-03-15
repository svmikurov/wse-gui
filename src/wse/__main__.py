"""Start the application."""

import logging

from wse.main import main

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    app = main()
    if app:
        app.main_loop()
    else:
        logger.error('Failed to initialize application')
