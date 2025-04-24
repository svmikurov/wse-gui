"""Defines Swarm control panel container."""

import toga

from wse.core.i18n import _
from wse.features.base.container import BaseContainer


class SwarmControlPanel(BaseContainer):
    """Swarm control panel."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the panel."""
        super().__init__(*args, **kwargs)

        # Construct UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self.base_url_input,
            self.endpoint_input,
            self.method,
        )

    def _create_ui(self) -> None:
        self.base_url_input = toga.TextInput()
        self.endpoint_input = toga.TextInput()
        self.method = toga.Selection()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self.base_url_input.placeholder = _('base url')
        self.endpoint_input.placeholder = _('endpoint')
