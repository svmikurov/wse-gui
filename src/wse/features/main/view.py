"""Defines the main screen view."""

import toga

from wse.config.config import Settings
from wse.core.logger import setup_logger
from wse.core.navigation.routes import Routes
from wse.features.shared.observer import Subject
from wse.features.shared.ui.box import ColumnFlexBox
from wse.features.shared.ui.button import ButtonStyled
from wse.features.shared.ui.heading import Heading
from wse.features.shared.ui.text import MultilineInfoPanel
from wse.utils.i18n import I18N, _

logger = setup_logger('HomeView')


class HomeView(ColumnFlexBox, Subject):
    """Represents the home screen."""

    def __init__(self) -> None:
        """Construct the view."""
        super().__init__()
        Subject.__init__(self)
        self._create_widgets()
        self._add_widgets_to_view()
        self.i18n = I18N(Settings())
        I18N.add_listener(self)

    def _create_widgets(self) -> None:
        self.heading = Heading(_('Home'))
        self.info_panel = MultilineInfoPanel()
        self.exercise_button = ButtonStyled(
            _('Exercises'), on_press=self._on_exercises_click
        )
        self.language_button = ButtonStyled(
            _('Switch Language'), on_press=self._on_switch_language
        )

    def _add_widgets_to_view(self) -> None:
        self.add(
            self.heading,
            self.info_panel,
            self.exercise_button,
            self.language_button,
        )

    ####################################################################
    # Widget handlers

    def _on_exercises_click(self, _: toga.Widget) -> None:
        self.notify('navigate', route=Routes.EXERCISES)

    def _on_switch_language(self, _: toga.Widget) -> None:
        current_lang = self.i18n.get_current_language()
        new_lang = 'ru' if current_lang == 'en' else 'en'
        self.i18n.set_language(new_lang)

    ####################################################################
    # Listener methods

    def language_changed(self) -> None:
        """Update texts when language changes."""
        self.heading.text = _('Home')
        self.exercise_button.text = _('Exercises')
        self.language_button.text = _('Switch Language')
