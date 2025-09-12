"""Home screen view."""

import logging
from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.interfaces.iwidgets import NavigableButton
from wse.utils.i18n import label_, nav_

from .abc import (
    HomeViewABC,
    HomeViewModelABC,
)

logger = logging.getLogger(__name__)


@inject
@dataclass
class HomeView(HomeViewABC):
    """Home screen view."""

    _state: HomeViewModelABC

    @override
    def __post_init__(self) -> None:
        super().__post_init__()
        self._content.test_id = NavID.HOME
        self._state.add_observer(self)

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._label_title,
            self._btn_assigned,
            self._btn_math,
            self._btn_account,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_assigned = self._create_nav_btn(nav_id=NavID.ASSIGNED)
        self._btn_math = self._create_nav_btn(nav_id=NavID.INDEX_MATH)
        self._btn_account = self._create_nav_btn(nav_id=NavID.LOGIN)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_assigned.style.update(**config.btn_nav)
        self._btn_math.style.update(**config.btn_nav)
        self._btn_account.style.update(**config.btn_nav)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Home page title')
        self._btn_assigned.text = nav_(NavID.ASSIGNED)
        self._btn_math.text = nav_(NavID.INDEX_MATH)
        self._btn_account.text = nav_(NavID.ACCOUNT)

    # UI state observe

    @override
    def user_authenticated(self) -> None:
        """Handle user 'authenticated' status."""
        logger.warning('Called not implemented `user_authenticated` method')

    @override
    def user_anonymous(self) -> None:
        """Handle user 'anonymous' status."""
        logger.warning('Called not implemented `user_anonymous` method')

    # Callback

    # TODO: Move to view base class.
    #       Add to view base class the generic type of ViewModel.
    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
        self._state.navigate(button.nav_id)
