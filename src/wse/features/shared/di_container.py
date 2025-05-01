"""Defines dependency injection containers for share."""

from dependency_injector import containers, providers

from wse.config.settings import STYLES
from wse.features.base.context import Context
from wse.features.shared.content import BaseContent, SimpleContent
from wse.features.shared.observer import Subject
from wse.features.shared.ui.button import ButtonFactory, ButtonHandler
from wse.features.shared.ui.keypad import DigitKeypad
from wse.features.shared.ui.ui_text import SingleLineDisplay


class ShareContainer(containers.DeclarativeContainer):
    """Share providers container."""

    # Injections
    content_box = providers.Factory(
        BaseContent,
    )
    context = providers.Factory(
        Context,
    )
    subject = providers.Factory(
        Subject,
    )
    simple_content = providers.Factory(
        SimpleContent,
    )
    button_factory = providers.Factory(
        ButtonFactory,
    )
    button_handler = providers.Factory(
        ButtonHandler,
        subject=subject,
    )

    # UI
    style_config = providers.Configuration(
        yaml_files=[
            STYLES / 'styles.yaml',
        ]
    )

    single_line_display = providers.Factory(
        SingleLineDisplay,
        content=simple_content,
        style_config=style_config,
    )

    digit_keypad = providers.Factory(
        DigitKeypad,
        handler=button_handler,
        content=simple_content,
        button_factory=button_factory,
    )
