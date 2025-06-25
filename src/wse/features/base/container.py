"""Defines abstract base class for widget containers."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from wse.features.base.mixins import AddObserverMixin, GetContentMixin
from wse.features.interfaces import IContent, ISubject


@dataclass
class BaseContainer(
    GetContentMixin,
    AddObserverMixin,
    ABC,
):
    """Abstract base class for widget container."""

    _content: IContent
    _subject: ISubject

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._setup()
        self.localize_ui()
        self._populate_content()

    def _setup(self) -> None:
        """Set up container features.

        Add features:
            - Content test ID
            - ...

        For example:
            def setup(self) -> None:
                self._content.test_id = NavID.HOME
                ...
        """
        pass

    @abstractmethod
    def _create_ui(self) -> None:
        """Create UI.

        For example:
            def _create_ui(self) -> None:
                self._label_title = toga.Label('')
                ...
        """

    @abstractmethod
    def localize_ui(self) -> None:
        """Localize the UI text.

        For example:
            def localize_ui(self) -> None:
                self._label_title.text = label_('Home page title')
                ...
        """

    @abstractmethod
    def _populate_content(self) -> None:
        """Populate widget container content with UI.

        For example:
            def _populate_content(self) -> None:
                self._content.add(
                    self._label_title,
                    ...
                )
        """
