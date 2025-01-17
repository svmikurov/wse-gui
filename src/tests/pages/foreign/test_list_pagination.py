"""Test pagination buttons of foreign word list page box."""

from unittest.mock import MagicMock, patch

import pytest

from tests.utils import FixtureReader
from wse.app import WSE
from wse.pages import SelectedForeignPage

URL_PAGINATION = 'http://127.0.0.1/api/v1/foreign/?limit=3&offset=3'


@pytest.fixture
def box_list(wse: WSE) -> SelectedForeignPage:
    """Return the tested box-container, fixture."""
    return wse.box_foreign_selected


@patch('httpx.Client.get')
def test_pagination_first_page(
    get: MagicMock,
    box_list: SelectedForeignPage,
) -> None:
    """Test pagination buttons at first page."""
    get.return_value = FixtureReader('pagination_foreign_first.json')

    btn_previous = box_list._btn_previous
    btn_next = box_list._btn_next

    # Populate a table.
    box_list.populate_table()

    # Previous button is not enabled.
    assert btn_previous.enabled is False

    # Next button is enabled.
    assert btn_next.enabled is True

    # Simulate a next button press.
    btn_next._impl.simulate_press()

    # Assert request next page.
    get.assert_called_with(URL_PAGINATION)


@patch('httpx.Client.get')
def test_pagination_last_page(
    get: MagicMock,
    box_list: SelectedForeignPage,
) -> None:
    """Test pagination buttons at last page."""
    get.return_value = FixtureReader('pagination_foreign_last.json')

    btn_previous = box_list._btn_previous
    btn_next = box_list._btn_next

    # Populate a table.
    box_list.populate_table()

    # Previous button is enabled.
    assert btn_previous.enabled is True

    # Next button is not enabled.
    assert btn_next.enabled is False

    # Simulate a previous button press.
    btn_previous._impl.simulate_press()

    # Assert request previous page.
    get.assert_called_with(URL_PAGINATION)


def test_btn_text(box_list: SelectedForeignPage) -> None:
    """Test the handler of button pagination next."""
    assert box_list._btn_previous.text == '<'
    assert box_list._btn_table_reload.text == 'Обновить'
    assert box_list._btn_next.text == '>'
