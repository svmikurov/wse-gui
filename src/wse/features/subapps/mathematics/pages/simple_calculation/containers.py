"""Defines UI containers for Simple Math Calculation page."""

from dataclasses import dataclass

from injector import inject

from wse.config.layout import TextExerciseStyleConfig, TextExerciseThemeConfig
from wse.features.shared.containers.base import BaseTextIOContainer
from wse.utils.i18n import label_


@inject
@dataclass
class SimpleMathCalcContainer(BaseTextIOContainer):
    """Simple Math calculation exercise container."""

    _style_config: TextExerciseStyleConfig
    _theme_config: TextExerciseThemeConfig

    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self.update_style(self._style_config)
        self.update_style(self._theme_config)

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._output_label.text = label_('Question')
        self._input_label.text = label_('Answer')

    def update_style(
        self, config: TextExerciseStyleConfig | TextExerciseThemeConfig
    ) -> None:
        """Update widgets style."""
        self._output_label.style.update(**config.label)
        self._output_text.style.update(**config.output_text)
        self._input_label.style.update(**config.label)
        self._input_text.style.update(**config.input_text)
