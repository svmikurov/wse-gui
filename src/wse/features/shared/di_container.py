"""Defines dependency injection containers for share."""

from dependency_injector import containers, providers

from wse.features.base.context import Context
from wse.features.shared.content import BaseContent, SimpleContent
from wse.features.shared.observer import IDSubject, Subject
from wse.features.shared.ui.di_conatiner import UIContainer


class ShareContainer(containers.DeclarativeContainer):
    """Share providers container."""

    content_box = providers.Factory(
        BaseContent,
    )
    context = providers.Factory(
        Context,
    )
    subject = providers.Factory(
        Subject,
    )
    id_subject = providers.Factory(
        IDSubject,
    )
    simple_content = providers.Factory(
        SimpleContent,
    )

    ui_container = providers.Container(
        UIContainer,
        subject=subject,
        id_subject=id_subject,
        simple_content=simple_content,
    )

    # API
    display_model = ui_container.display_model
    keypad_model = ui_container.keypad_model
    line_display = ui_container.line_display
    digit_keypad = ui_container.digit_keypad
    style_config = ui_container.style_config
    button_handler = ui_container.button_handler
