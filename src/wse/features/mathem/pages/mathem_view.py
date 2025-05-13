"""Mathematical feature view (MVC)."""

import dataclasses
import logging

import toga

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavID
from wse.features.base.mvc_ import BaseView
from wse.features.mathem.interfaces.ipages import IMathematicalView
from wse.features.mathem.sources import SourceHub
from wse.features.shared.enums import StyleID
from wse.features.shared.enums.object_id import ObjectID
from wse.features.shared.ui.ui_text import TextPanel
from wse.interface.iobserver import ISubject

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class MathematicalView(BaseView, IMathematicalView):
    """View for mathematical exercises page."""

    _subject: ISubject

    def __post_init__(self) -> None:
        """Post init."""
        super().__post_init__()
        self._content.id = ObjectID.MATHEMATICAL

    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self.exercise_selection,
            self.text_panel,
            self._btn_goto_calculate,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        """Create a user interface."""
        self._label_title = toga.Label('')
        self.exercise_selection: toga.Selection = toga.Selection(
            accessor='name',
            items=SourceHub(),
            on_change=self.switch_exercise,  # type: ignore
        )
        self.text_panel = TextPanel()
        self._btn_goto_calculate = self._create_nav_btn()
        self._btn_back = self._create_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._label_title.text = _('Mathematical title')
        self.exercise_selection.text = _('Select exercise')
        self._btn_goto_calculate.text = _(NavID.MATH_CALCULATION)
        self._btn_back.text = _(NavID.BACK)

    # Style Management

    @property
    def _ui_styles(self) -> dict[toga.Widget, StyleID]:
        return {
            self._label_title: StyleID.TITLE,
            self._btn_goto_calculate: StyleID.DEFAULT_BUTTON,
            self._btn_back: StyleID.DEFAULT_BUTTON,
            self.exercise_selection: StyleID.NO_STYLE,
        }

    # Notifications

    @property
    def subject(self) -> ISubject:
        """Get subject of Observer pattern."""
        return self._subject

    def switch_exercise(self, widget: toga.Selection) -> None:
        """Notify that exercise selected with selection UI."""
        try:
            self.subject.notify(
                'switch_exercise',
                value=widget.value.name,  # type: ignore
            )
            logger.info(f'Selected "{widget.value.name}" exercise')  # type: ignore
        except AttributeError:
            logger.debug('Selections has no element with "name" attr')
