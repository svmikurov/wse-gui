"""Defines top bar container.

Contains mixins for page components to control top bar containers.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Generic, Type, TypeVar

import toga
from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.utils.i18n import nav_

from ...base.mixins import NotifyNavigateMixin
from ...interfaces.icontent import IContent
from ...interfaces.iobserver import ISubject
from ..widgets.interfaces import IFlexRowStub
from .iabc.itop_bar import (
    BaseTopBarContainer,
    BaseTopBarController,
    ITopBarContainer,
    ITopBarController,
    ITopBarPageViewMixin,
)

TopBarView = TypeVar('TopBarView', bound=ITopBarPageViewMixin)


@inject
@dataclass
class TopBarContainer(
    BaseTopBarContainer,
):
    """Top bar container."""

    _style: StyleConfig
    _theme: ThemeConfig
    _flex_stub: Type[IFlexRowStub]

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


@inject
@dataclass
class TopBarController(
    BaseTopBarController,
):
    """Top bar controller."""

    _container: ITopBarContainer

    @override
    def _setup(self) -> None:
        super()._setup()
        self._container.add_observer(self)

    @property
    @override
    def content(self) -> IContent:
        """Get container content."""
        return self._container.content

    # API for view

    @override
    def update_balance(self, value: str) -> None:
        """Handle the balance update notification."""
        self._container.update_balance(value)


# Mixins for page MVC model components


class TopBarModelMixin:
    """Mixin providing top bar features for page model."""

    _subject: ISubject

    def _notify_balance_updated(self, value: Decimal) -> None:
        """Notify than balance updated."""
        self._subject.notify('balance_update', value=value)


@inject
@dataclass
class TopBarPageViewMixin(
    NotifyNavigateMixin,
):
    """Mixin providing top bar features for page view.

    Used with `ContainerABC` derived classes.
    """

    _top_bar: ITopBarController

    def _setup(self) -> None:
        super()._setup()  # type: ignore[misc]
        self._top_bar.add_observer(self)

    # API for page controller

    def update_balance(self, value: str) -> None:
        """Update balance."""
        self._top_bar.update_balance(value)


class TopBarPageControllerMixin(Generic[TopBarView]):
    """Mixin providing top bar features for page controller."""

    _view: TopBarView

    # Notification from page model

    def balance_update(self, value: str) -> None:
        """Handle balance update event notification."""
        self._view.update_balance(value)
