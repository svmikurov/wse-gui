"""Defines top bar container."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import (
    TopBarStyle,
    TopBarTheme,
)
from wse.utils.i18n import _, nav_

from ...base.container import NavigableContainer
from ...base.mixins import AddObserverMixin, NotifyNavigateMixin
from ...base.mvc import BaseController
from ...interfaces import IContent
from ...subapps.nav_id import NavID
from ..widgets.interfaces import IFlexRowStub
from .interfaces import ITopBarContainer, ITopBarController


@inject
@dataclass
class TopBarContainer(
    NavigableContainer[TopBarStyle, TopBarTheme],
):
    """Top bar container."""

    _style_config: TopBarStyle
    _theme_config: TopBarTheme
    _flex_stub: Type[IFlexRowStub]

    @override
    def _setup(self) -> None:
        super()._setup()
        self.localize_ui()
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
        self._label_balance.text = _('Balance')

    def update_style(self, config: TopBarStyle | TopBarTheme) -> None:
        """Update widgets style."""
        self._btn_back.style.update(**config.button)
        self._label_balance.style.update(**config.label_balance)


@inject
@dataclass
class TopBarController(
    AddObserverMixin,
    BaseController,
    NotifyNavigateMixin,
    ITopBarController,
):
    """Top bar controller."""

    _container: ITopBarContainer

    @override
    def _setup(self) -> None:
        self._container.add_observer(self)

    @property
    def content(self) -> IContent:
        """Get container content."""
        return self._container.content
