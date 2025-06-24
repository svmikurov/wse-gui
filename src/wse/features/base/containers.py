"""Defines abstract base class for widget containers."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import toga

from wse.config.layout import StyleConfig, ThemeConfig
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
    _style_config: StyleConfig
    _theme_config: ThemeConfig

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self.localize_ui()
        self.update_style(self._style_config)
        self.update_style(self._theme_config)
        self._populate_content()
        self._setup()

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
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style.

        For example:
            def update_style(
                self, config: StyleConfig | ThemeConfig
            ) -> None:
                self._label_title.style.update(**config.title)
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


@dataclass
class IOTextContainer(BaseContainer, ABC):
    """Abstract base class for I/O one line text container."""

    def _populate_content(self) -> None:
        self.content.add(
            self._output_label,
            self._output_text,
            self._input_label,
            self._input_text,
        )

    def _create_ui(self) -> None:
        self._output_label = toga.Label('')
        self._output_text = toga.Label('')
        self._input_label = toga.Label('')
        self._input_text = toga.TextInput()
