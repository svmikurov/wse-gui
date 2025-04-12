"""Defines login page model."""

from wse.features.base.mvc import BaseModel


class LoginModel(BaseModel):
    """Login page model."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the model."""
        super().__init__(*args, **kwargs)

    def _set_context(self) -> None:
        """Set view context for render into view."""
        ...

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""
        ...
