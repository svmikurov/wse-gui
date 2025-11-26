"""Word study Presentation parameters Screen tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from wse.ui.foreign.params import view

if TYPE_CHECKING:
    from wse.ui.foreign.params import view


class TestScreenInitialization:
    """Word study Presentation parameters Screen initialize tests."""

    def test_initialization_success(
        self,
        screen: view.WordStudyParamsView,
    ) -> None:
        """Test that screen is initialized successfully."""
        # Assert
        assert screen
