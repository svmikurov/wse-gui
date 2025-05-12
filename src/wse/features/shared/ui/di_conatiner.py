"""Defines dependency injection containers for share UI."""

from dependency_injector import containers, providers

from wse.config.settings import STYLES_PATH
from wse.features.shared.ui.button import ButtonHandler
from wse.features.shared.ui.keypad import DigitKeypad
from wse.features.shared.ui.ui_text import LineDisplay
from wse.features.shared.ui.ui_text_model import DisplayModel, KeypadModel


class UIContainer(containers.DeclarativeContainer):
    """UI dependency injection container."""

    # Configurations
    style_config = providers.Configuration(
        yaml_files=[
            STYLES_PATH / 'styles.yaml',
        ]
    )

    # Dependencies
    subject = providers.Dependency()
    id_subject = providers.Dependency()
    simple_content = providers.Dependency()

    # Buttons helpers
    button_handler = providers.Factory(
        ButtonHandler,
        subject=subject,
    )

    # Text / digit display
    display_model = providers.Factory(
        DisplayModel,
        _subject=subject,
    )
    keypad_model = providers.Factory(
        KeypadModel,
        _subject=id_subject,
    )
    line_display = providers.Factory(
        LineDisplay,
        content=simple_content,
        style_config=style_config,
    )

    # Digit keypad
    digit_keypad = providers.Factory(
        DigitKeypad,
        _content=simple_content,
        _button_handler=button_handler,
        _style_config=style_config,
    )
