"""Defines top bar container."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation.nav_id import NavID
from wse.feature.observer.mixins import SubjectGen
from wse.ui.base.content.abc import ContentABC
from wse.ui.base.iwidgets import NavigableButton
from wse.ui.base.navigate import CreateNavButtonABC, NavigateABC
from wse.ui.widgets import FlexRowStubType
from wse.utils.i18n import nav_

from .abc import NotifyT, TopBarContainerABC, TopBarControllerABC


@inject
@dataclass
class TopBarContainer(
    SubjectGen[NavigateABC, NotifyT],
    CreateNavButtonABC,
    TopBarContainerABC,
):
    """Top bar container."""

    _style: StyleConfig
    _theme: ThemeConfig
    _flex_stub: FlexRowStubType

    @override
    def _create_ui(self) -> None:
        """Create UI."""
        self._btn_back = self._create_nav_btn(NavID.BACK)
        self._label_balance = toga.Label('')

    @override
    def _populate_content(self) -> None:
        """Populate widget container content with UI."""
        self._content.add(
            self._btn_back,
            self._flex_stub(),
            self._label_balance,
        )

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._btn_back.text = nav_(NavID.BACK)
        self._label_balance.text = ''

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._content.style.direction = 'row'
        self._btn_back.style.update(**config.top_bar.button)
        self._label_balance.style.update(**config.top_bar.label_balance)

    # API for controller

    def update_balance(self, value: str) -> None:
        """Update balance label."""
        self._label_balance.text = value

    # Navigation callback

    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
        self._subject.notify('navigate', nav_id=button.nav_id)

    @property
    def content(self) -> ContentABC:
        """Get page content."""
        return self._content


@inject
@dataclass
class TopBarController(
    TopBarControllerABC,
):
    """Top bar controller."""

    _container: TopBarContainerABC

    def __post_init__(self) -> None:
        """Construct the controller."""
        self._container.add_observer(self)

    @property
    @override
    def content(self) -> ContentABC:
        """Get container content."""
        return self._container.content

    # API for view

    @override
    def update_balance(self, value: str) -> None:
        """Handle the balance update notification."""
        self._container.update_balance(value)
