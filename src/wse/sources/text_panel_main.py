"""The source of info text panel at main pages."""

from toga.sources import Source

from wse.constants import HOST
from wse.models.user import User


class SourceMainPanel(Source):
    """The info text panel source."""

    welcome = f'Ready for connect to {HOST}'
    """Welcome text on the information display (`str`).
    """
    text_user_info = 'Добро пожаловать, %s!'
    """User info text (`str`).
    """

    def __init__(self, user: User) -> None:
        """Construct the source."""
        super().__init__()
        self._value = ''
        self.user = user

    def update_text(self) -> None:
        """Update info text by user auth status."""
        if self.user.is_auth:
            self._value = self.text_user_info % self.user.username
        else:
            self._value = self.welcome

    @property
    def value(self) -> str | None:
        """Return text to display (`str`, reade-only)."""
        self.update_text()
        return self._value
