"""Test start app."""

from wse.app import WSE


def test_start(
    wse: WSE,
) -> None:
    """Test start app."""
    assert wse.main_window.content is wse.box_main
