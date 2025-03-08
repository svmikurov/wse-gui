"""Defines the data model for the authentication feature."""


class UserModel:
    """User model."""

    def __init__(self) -> None:
        """Construct the model."""
        super().__init__()
        self.username: str | None = None
        self.password: str | None = None
