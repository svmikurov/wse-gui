"""Test foreign main page box widgets.

Testing:
 * Text representation of widgets in the window content
   (text on widget).
 * Changing window contents when pressing move buttons.
 * The order of widget at page.
"""

from unittest.mock import MagicMock, patch

import pytest
from _pytest.monkeypatch import MonkeyPatch
from httpx import Client

from tests.utils import FixtureReader, run_until_complete
from wse.app import WSE

FIXTURE = 'response_foreign_list.json'
"""The fixture file name of json http response with a list of word
(`str`).
"""


@pytest.fixture(autouse=True)
def goto_foreign_page_box(wse: WSE) -> None:
    """Assign the foreign main box to main window content, fixture."""
    wse.main_window.content = wse.box_foreign_main


def mock_list_json(*args: object, **kwargs: object) -> FixtureReader:
    """Mock a json http response with a list of terms."""
    return FixtureReader(FIXTURE)


def test_label_title(wse: WSE) -> None:
    """Test label of page box title."""
    # Label text.
    title = wse.box_foreign_main.label_title
    assert title.text == 'Иностранный словарь'


def test_btn_goto_create(wse: WSE) -> None:
    """Test the button go to foreign create page box."""
    btn = wse.box_foreign_main.btn_goto_create
    assert btn.text == 'Добавить слово'

    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Window switching.
    assert wse.main_window.content == wse.box_foreign_create


@patch('httpx.Client.get')
def test_btn_goto_params(
    get: MagicMock,
    wse: WSE,
) -> None:
    """Test the button go to foreign exercise params page box.

    Mock:
     * ``get`` method of httpx.Client, otherwise http request.
    """
    btn = wse.box_foreign_main.btn_goto_params

    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    assert btn.text == 'Упражнение'

    # Window switching.
    assert wse.main_window.content == wse.box_foreign_params


def test_btn_goto_list(wse: WSE, monkeypatch: MonkeyPatch) -> None:
    """Test the button go to foreign word list page box."""
    btn = wse.box_foreign_main.btn_goto_list
    assert btn.text == 'Словарь иностранных слов'

    # Window switching.
    # Switching to the list page calls the http request of word list to
    # populate the table.
    # If mapping of word list have not required fields will be raising
    # the KeyError.
    monkeypatch.setattr(Client, 'get', mock_list_json)

    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    assert wse.main_window.content == wse.box_foreign_selected
