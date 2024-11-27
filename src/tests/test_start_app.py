"""Test start app."""

from unittest.mock import MagicMock, patch

from wse.app import WSE


@patch('httpx.Client.get')
def test_start(
    get: MagicMock,
    wse: WSE,
) -> None:
    """Test start app."""
    assert wse.main_window.content is wse.box_main
