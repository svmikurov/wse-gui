"""Test pagination buttons of foreign word list page box.

Testing:
 * Text representation of widgets in the window content
   (text on widget, placeholder text).
 * Button handlers.
"""

from unittest.mock import MagicMock, patch

import pytest
from _pytest.monkeypatch import MonkeyPatch
from httpx import Client

from tests.utils import FixtureReader
from wse.app import WSE
from wse.pages import ListForeignPage

FIXTURE_PAGINATION_FIRST = 'pagination_foreign_first.json'
"""The fixture file name to test the first pagination page (`str`)."""
FIXTURE_PAGINATION_LAST = 'pagination_foreign_last.json'
"""The fixture file name to test the last pagination page (`str`)."""


@pytest.fixture
def box_list(wse: WSE) -> ListForeignPage:
    """Return the tested box-container, fixture."""
    return wse.box_foreign_list


def mock_pagination_first(*args: object, **kwargs: object) -> FixtureReader:
    """Return a json http response to test the first pagination page."""
    return FixtureReader(FIXTURE_PAGINATION_FIRST)


def mock_pagination_last(*args: object, **kwargs: object) -> FixtureReader:
    """Return a json http response to test the last pagination page."""
    return FixtureReader(FIXTURE_PAGINATION_LAST)


def test_pagination_first_page(
    box_list: ListForeignPage,
    monkeypatch: MonkeyPatch,
) -> None:
    """Test pagination buttons at first page."""
    btn_previous = box_list._btn_previous
    btn_next = box_list._btn_next

    # Mock http request word list in first page.
    monkeypatch.setattr(Client, 'get', mock_pagination_first)

    # Populate a table.
    box_list.populate_table()

    # Previous button is not enabled.
    assert btn_previous.enabled is False

    # Next button is enabled.
    assert btn_next.enabled is True


def test_pagination_last_page(
    box_list: ListForeignPage,
    monkeypatch: MonkeyPatch,
) -> None:
    """Test pagination buttons at last page."""
    btn_previous = box_list._btn_previous
    btn_next = box_list._btn_next

    # Mock http request word list in last page.
    monkeypatch.setattr(Client, 'get', mock_pagination_last)

    # Populate a table.
    box_list.populate_table()

    # Previous button is enabled.
    assert btn_previous.enabled is True

    # Next button is not enabled.
    assert btn_next.enabled is False


@patch('httpx.Client.get')
def test_btn_next_handler(
    get: MagicMock,
    box_list: ListForeignPage,
) -> None:
    """Test the handler of button pagination next."""
    btn = box_list._btn_next
    btn.enabled = True

    btn._impl.simulate_press()

    assert btn.text == '>'

    assert get.called


@patch('httpx.Client.get')
def test_btn_previous_handler(
    get: MagicMock,
    box_list: ListForeignPage,
) -> None:
    """Test the handler of button pagination previous."""
    btn = box_list._btn_previous
    btn.enabled = True

    btn._impl.simulate_press()

    assert btn.text == '<'

    assert get.called


@patch('httpx.Client')
def test_btn_table_reload_handler(client: MagicMock, wse: WSE) -> None:
    """Test the handler of button pagination previous."""
    btn = wse.box_foreign_list._btn_table_reload
    assert btn.text == 'Обновить'

    btn.enabled = True
    btn._impl.simulate_press()
    assert client.called
