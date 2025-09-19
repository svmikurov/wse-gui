"""Defines top bar container."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation.nav_id import NavID
from wse.feature.base.mixins import AddObserverMixin
from wse.feature.interfaces.icontent import ContentProto
from wse.feature.interfaces.iwidgets import NavigableButton
from wse.feature.shared.widgets import FlexRowStubProto
from wse.ui.base.abc.navigate import CreateNavButtonABC
from wse.utils.i18n import nav_

from ..top_bar.itop_bar import (
    TopBarContainerProto,
)
from .abc import TopBarContainerABC, TopBarControllerABC


@inject
@dataclass
class TopBarContainer(
    AddObserverMixin,
    CreateNavButtonABC,
    TopBarContainerABC,
):
    """Top bar container."""

    _style: StyleConfig
    _theme: ThemeConfig
    _flex_stub: Type[FlexRowStubProto]

    @override
    def _setup(self) -> None:
        super()._setup()
        # TODO: Fix direction style changing
        self._content.style.direction = 'row'

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


@inject
@dataclass
class TopBarController(
    TopBarControllerABC,
):
    """Top bar controller."""

    _container: TopBarContainerProto

    @override
    def _setup(self) -> None:
        super()._setup()
        self._container.add_observer(self)

    @property
    @override
    def content(self) -> ContentProto:
        """Get container content."""
        return self._container.content

    # API for view

    @override
    def update_balance(self, value: str) -> None:
        """Handle the balance update notification."""
        self._container.update_balance(value)
