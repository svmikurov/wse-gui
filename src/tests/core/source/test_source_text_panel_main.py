"""Unit tests of source info text panel at main page."""

from unittest.mock import MagicMock, PropertyMock, patch

import pytest

from wse.app import WSE
from wse.constants import HOST_API
from wse.source.text_panel_main import MainTextPanelSource


@pytest.fixture
def source(wse: WSE) -> MainTextPanelSource:
    """Return the info text panel instance, fixture."""
    return MainTextPanelSource(wse.user)


def test_display_on_start_app() -> None:
    """Test the text display on start app, user not auth."""
    welcome = f'Ready for connect to {HOST_API}'

    # Create app instance on start app.
    wse = WSE(formal_name='Test app', app_id='com.com')

    # Info panel text for not auth user.
    assert wse.box_main.info_panel.value == welcome


@patch(
    'wse.source.text_panel_main.MainTextPanelSource.value',
    new_callable=PropertyMock,
)
def test_call_on_start(
    mock: MagicMock,
) -> None:
    """Test source calls on start app."""
    # Create app instance on start app.
    WSE(formal_name='Test app', app_id='com.com')

    # Get info text.
    mock.assert_called_once()