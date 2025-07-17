"""Defines view content implementation."""

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import ThemeConfig

from ..interfaces.icontent import IContent
from ..subapps.nav_id import NavID


class Content(toga.Box, IContent):  # type: ignore[misc]
    """Page content."""

    @inject
    def __init__(
        self,
        theme_config: ThemeConfig,
    ) -> None:
        """Construct the content."""
        style = {
            **theme_config.content,
            'direction': 'column',
        }
        super().__init__(**style)
        self._test_id: NavID | None = None

    @override
    @property
    def test_id(self) -> NavID | None:
        """Get test ID."""
        return self._test_id

    @test_id.setter
    def test_id(self, value: NavID | None) -> None:
        self._test_id = value
