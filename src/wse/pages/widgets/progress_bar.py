"""Custom progress bar.

Make widget a listener.
"""

import toga


class ProgressBarApp(toga.ProgressBar):
    """Custom progress bar."""

    def increase(self, step_size: int | float) -> None:
        """Increase the progress bar value."""
        self.value += step_size

    def reset(self) -> None:
        """Reset the progress."""
        self.value = 0.0
