"""Foreign words study View."""

import logging
from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation import NavID
from wse.domain.foreign import ExerciseAccessorT
from wse.feature.observer.generic import HandleObserverGenABC
from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateViewMixin
from wse.ui.containers.control import Action, ControlContainerABC
from wse.ui.containers.info.abc import InfoContainerABC
from wse.ui.containers.presentation import PresentationContainerABC
from wse.ui.containers.top_bar.abc import TopBarControllerABC

from . import StudyForeignViewABC, WordPresentationViewModelABC, state

log = logging.getLogger(__name__)


@inject
@dataclass
class StudyForeignView(
    ObserverManagerGen[HandleObserverGenABC[Action]],
    NavigateViewMixin,
    StudyForeignViewABC,
):
    """Foreign words study View."""

    _state: WordPresentationViewModelABC
    _top_bar: TopBarControllerABC
    _presentation_container: PresentationContainerABC
    _control_container: ControlContainerABC
    _info_container: InfoContainerABC

    @override
    def __post_init__(self) -> None:
        """Configure the view."""
        self._top_bar.add_observer(self)
        self._state.add_observer(self)
        self._control_container.add_observer(self)
        self._content.test_id = NavID.FOREIGN_STUDY
        super().__post_init__()

    @override
    def _create_ui(self) -> None:
        self._title = toga.Label(NavID.FOREIGN_STUDY)
        self._progress_bar = toga.ProgressBar()

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._progress_bar,
            self._top_bar.content,
            self._title,
            self._presentation_container.content,
            self._info_container.content,
            toga.Box(flex=1),
            self._control_container.content,
        )

    @override
    def localize_ui(self) -> None:
        return

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        self._title.style.update(**config.label_title)

    def on_open(self) -> None:
        """Call methods on screen open."""
        self._state.on_open()

    # TODO: Add to base class the subject
    # if `on_close` method is not define?
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)
        self._state.remove_observer(self)
        self._control_container.remove_observer(self)
        self._state.on_close()

    # Observer methods
    # ----------------

    @override
    def handle(self, action: Action) -> None:
        """Handle user action.

        Observes the control container.
        """
        self._state.handle(action)

    # TODO: Refactor
    def timeout_updated(self, accessor: str, max: float, value: float) -> None:
        """Update progress bar."""
        self._progress_bar.max = max if max else 0.1
        self._progress_bar.value = value

    @override
    def pause_state_updated(self, value: bool) -> None:
        """Update pause state."""
        self._control_container.update_pause_state(value)

    @override
    def unknown_state_updated(self, value: bool) -> None:
        """Update unknown state."""
        self._control_container.update_unknown_state(value)

    @override
    def change(self, accessor: ExerciseAccessorT, value: object) -> None:
        """Change ui context via accessor."""
        match accessor:
            case 'definition' | 'explanation':
                self._presentation_container.change(accessor, value)

            case 'info':
                if isinstance(value, state.TextInfo):
                    for k, v in value._asdict().items():
                        self._info_container.change(k, v)
                else:
                    log.warning(f'Expected `TextInfo`, got `{type(accessor)}`')

            case _:
                log.warning(f'Unhandled accessor: {accessor}')
