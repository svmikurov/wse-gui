"""Word study params View."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation import NavID

# TODO: Rename 'wse.ui.base.iwidgets'
from wse.ui.base.iwidgets import NavigableButton
from wse.ui.base.navigate.mixin import NavigateViewMixin
from wse.ui.containers.params import ParamsAccessorEnum, ParamsContainerABC
from wse.ui.containers.top_bar.abc import TopBarControllerABC
from wse.ui.widgets.buttons import NavButton
from wse.utils import I18N

from . import WordStudyParamsViewABC, WordStudyParamsViewModelABC


@inject
@dataclass
class WordStudyParamsView(
    NavigateViewMixin,
    WordStudyParamsViewABC,
):
    """Word study params View."""

    _top_bar: TopBarControllerABC
    _state: WordStudyParamsViewModelABC
    _params: ParamsContainerABC

    def __post_init__(self) -> None:
        """Construct the View."""
        self._state.add_observer(self)
        self._top_bar.add_observer(self)
        self._params.add_observer(self)
        super().__post_init__()

    # TODO: Fix type ignore
    @override
    def _create_ui(self) -> None:
        self._title = toga.Label(I18N.NAV(NavID.FOREIGN_PARAMS))
        self._btn_save = toga.Button(
            I18N.EXERCISE('Save'),
            on_press=self._save_params,  # type: ignore[arg-type]
            flex=1,
        )
        self._btn_reset = toga.Button(
            I18N.EXERCISE('Reset'),
            on_press=self._reset_params,  # type: ignore[arg-type]
            flex=1,
        )
        self._btn_start = NavButton(
            text=I18N.EXERCISE(I18N.EXERCISE('Start')),
            nav_id=NavID.FOREIGN_STUDY,
            on_press=self._start_exercise,
            flex=1,
        )

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
            self._params.content,
            toga.Box(flex=1),
            toga.Box(
                children=[self._btn_reset, self._btn_save, self._btn_start]
            ),
        )

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._title.style.update(**config.label_title)
        self._btn_reset.style.update(**config.button)
        self._btn_save.style.update(**config.button)
        self._btn_start.style.update(**config.btn_nav)

    # TODO: Remove from abstract base?
    @override
    def localize_ui(self) -> None:
        """Localize widgets."""

    @override
    def on_open(self) -> None:
        """Call methods on screen open."""
        self._state.on_open()

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)
        self._params.remove_observer(self)
        self._state.remove_observer(self)
        self._state.on_close()

    # TODO: Move `_handle_navigate` to mixin?
    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press, top bar handler."""
        self._state.navigate(button.nav_id)

    # Notification observe
    # --------------------

    @override
    def values_updated(
        self,
        accessor: ParamsAccessorEnum,
        values: object,
    ) -> None:
        """Update Params container values via UIState notification."""
        self._params.set_values(accessor=accessor, values=values)

    @override
    def value_updated(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update Params container value via UIState notification."""
        self._params.set_value(accessor=accessor, value=value)

    @override
    def widget_updated(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update UIState via injected UI notification."""
        self._state.update_widget_state(accessor, value)

    # Widget callback functions
    # -------------------------

    def _save_params(self, _: toga.Button) -> None:
        self._state.save_params()

    def _reset_params(self, _: toga.Button) -> None:
        self._state.reset_params()

    def _start_exercise(self, _: toga.Button) -> None:
        self._state.start_exercise()
