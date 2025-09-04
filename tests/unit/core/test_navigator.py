"""Test the navigator feature."""

import unittest
from collections import deque
from unittest.mock import MagicMock

import toga

from wse.apps.main.pages.home import HomeControllerProto
from wse.apps.math.pages.index import MathControllerProto
from wse.apps.math.pages.simple_calc import CalculationControllerProto
from wse.apps.nav_id import NavID
from wse.core.navigation.navigator import Navigator
from wse.feature.interfaces.icontent import ContentProto


class TestNavigator(unittest.TestCase):
    """Test the Navigator service."""

    def setUp(self) -> None:
        """Set up the test."""
        self.mock_window = MagicMock(spec=toga.Window)

        self.mock_home_content = MagicMock(spec=ContentProto)
        self.mock_home_controller = MagicMock(spec=HomeControllerProto)
        self.mock_home_controller.content = self.mock_home_content

        self.mock_math_content = MagicMock(spec=ContentProto)
        self.mock_math_controller = MagicMock(spec=MathControllerProto)
        self.mock_math_controller.content = self.mock_math_content

        self.mock_calc_content = MagicMock(spec=ContentProto)
        self.mock_calc_controller = MagicMock(spec=CalculationControllerProto)
        self.mock_calc_controller.content = self.mock_calc_content

        self.routes = {
            NavID.HOME: self.mock_home_controller,
            NavID.INDEX_MATH: self.mock_math_controller,
            NavID.SIMPLE_CALC: self.mock_calc_controller,
        }

        self.navigator = Navigator(window=self.mock_window)
        self.navigator.set_routes(self.routes)  # type: ignore[arg-type]

    def test_initial_state(self) -> None:
        """Test initial state."""
        self.assertIsInstance(self.navigator._window, toga.Window)
        self.assertIsInstance(self.navigator._routes, dict)
        self.assertIsInstance(self.navigator._content_history, deque)
        self.assertEqual(len(self.navigator._content_history), 0)

    def test_navigation_flow(self) -> None:
        """Test complete navigation flow."""
        self.navigator.navigate(NavID.HOME)

        # Type checking
        self.assertEqual(self.mock_window.content.__class__, ContentProto)

        # Is assign necessary page content to window
        self.assertEqual(
            self.mock_window.content,
            self.mock_home_controller.content,
        )

        # Is added navigation ID to page history
        self.assertEqual(
            self.navigator._content_history[-1],
            NavID.HOME,
        )

    def test_back_navigation(self) -> None:
        """Test back navigation with history."""
        self.navigator._content_history = deque([NavID.HOME, NavID.INDEX_MATH])
        self.navigator.navigate(NavID.BACK)
        self.assertEqual(self.mock_window.content, self.mock_home_content)

    def test_content_history(self) -> None:
        """Test content history."""
        expected_history: deque[NavID] = deque(maxlen=10)
        walk = [
            NavID.HOME,
            NavID.INDEX_MATH,
            NavID.SIMPLE_CALC,
            NavID.BACK,
            NavID.SIMPLE_CALC,
            NavID.BACK,
            NavID.BACK,
            NavID.INDEX_MATH,
            NavID.SIMPLE_CALC,
            NavID.BACK,
            NavID.BACK,
        ]
        for nav_id in walk:
            if nav_id != NavID.BACK:
                expected_history.append(nav_id)
            else:
                expected_history.pop()

            self.navigator.navigate(nav_id)
            self.assertEqual(
                self.navigator._content_history,
                expected_history,
            )
