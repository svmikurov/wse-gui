import asyncio
import sys
from asyncio import AbstractEventLoop
from unittest.mock import MagicMock, patch

import pytest
import toga

from src.wse.config.config import PROJECT_PATH

import_path = str(PROJECT_PATH / 'src')
sys.path.insert(0, import_path)

from wse.app import WSE
from wse.main import main


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='function')
@patch('httpx.Client.get')
def wse(
    get: MagicMock,
    event_loop: AbstractEventLoop
) -> WSE:
    """Return the application instance, fixture."""
    # The app icon is cached; purge the app icon cache if it exists
    try:
        del toga.Icon.__APP_ICON
    except AttributeError:
        pass

    return main()
