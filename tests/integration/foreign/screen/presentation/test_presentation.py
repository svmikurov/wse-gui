"""Word study Presentation tests."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from wse.data.repos import foreign as repos
    from wse.ui.foreign.presentation import view


class TestScreenInitialization:
    """Word study Presentation parameters Screen initialize tests."""

    @pytest.mark.asyncio
    async def test_success(
        self,
        screen: view.WordPresentationView,
        parameters_repo: repos.WordParametersRepo,
    ) -> None:
        """Test that screen is initialized successfully."""
        # Act
        # Start presentation
        screen.on_open()

        # Time to start asynchronous tasks
        await asyncio.sleep(0.01)
