import asyncio

import pytest
import toga

from wse_gui.app import WSEGUI

FORMAL_NAME = 'Test App'
APP_ID = 'org.example.test'


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def app(event_loop):
    # The app icon is cached; purge the app icon cache if it exists
    try:
        del toga.Icon.__APP_ICON
    except AttributeError:
        pass

    app = WSEGUI(formal_name=FORMAL_NAME, app_id=APP_ID)

    return app
