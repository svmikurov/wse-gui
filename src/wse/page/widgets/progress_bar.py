"""Custom progress bar.

Make widget a listener.
"""

import toga


class ProgressBarApp(toga.ProgressBar):
    """Custom progress bar."""

    def set_max(self, max: int | float = 1.0) -> None:
        """Set max progress bar value."""
        self.max = max

    def increase(self, step_size: int | float = 0.0) -> None:
        """Increase the progress bar value."""
        self.value += step_size

    def reset(self) -> None:
        """Reset the progress."""
        self.value = 0.0
