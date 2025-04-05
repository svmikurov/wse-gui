"""Test the start application."""

from unittest.mock import MagicMock, patch

import pytest

from wse.application.app import WSE
from wse.features.obj_test_id import ObjectTestID


@pytest.mark.asyncio
@patch('httpx.AsyncClient.get')
async def test_start_app(_: MagicMock) -> None:
    """Test the start application."""
    app = WSE(formal_name='Test App', app_id='org.example.test')

    # The application starts with the home page displayed.
    assert app.main_window.content.test_id is ObjectTestID.HOME_VIEW
