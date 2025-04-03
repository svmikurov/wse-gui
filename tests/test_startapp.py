"""Test the start application."""

from unittest.mock import MagicMock, patch

import pytest

from wse.app import WSE


@pytest.mark.asyncio
@patch('httpx.AsyncClient.get')
async def test_start_app(_: MagicMock) -> None:
    """Test the start application."""
    app = WSE(formal_name='Test App', app_id='org.example.test')
    assert app.main_window.content == app.page_home.content
