"""Defines abstract base class for widget containers."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from injector import inject

from .. import StyleT, ThemeT
from ..base.mixins import (
    AddObserverMixin,
    CreateNavButtonMixin,
    GetContentMixin,
)
from .abstract.mvc import LocalizeMixin, UpdateStyle


@dataclass
class Container(
    GetContentMixin,
    ABC,
):
    """Abstract base class for widget container."""

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._setup()
        self._populate_content()

    def _setup(self) -> None:
        """Set up container features.

        Add features:
            - Content test ID
            - ...

        For example:

        .. code-block:: python

            def setup(self) -> None:
                self._content.test_id = NavID.HOME
                ...
        """
        pass

    @abstractmethod
    def _create_ui(self) -> None:
        """Create UI.

        For example:

        .. code-block:: python

            def _create_ui(self) -> None:
                self._label_title = toga.Label('')
                ...
        """

    @abstractmethod
    def _populate_content(self) -> None:
        """Populate widget container content with UI.

        For example:

        .. code-block:: python

            def _populate_content(self) -> None:
                self._content.add(
                    self._label_title,
                    ...,
                )
        """


@dataclass
class StyledContainer(
    Container,
    UpdateStyle[StyleT, ThemeT],
    ABC,
):
    """Abstract base class for styled widget container."""

    def _setup(self) -> None:
        super()._setup()
        self._apply_styles()


@inject
@dataclass
class LocaleContainer(
    StyledContainer[StyleT, ThemeT],
    LocalizeMixin,
    ABC,
):
    """Abstract base class for styled and localized widget container."""

    def _setup(self) -> None:
        super()._setup()
        self.localize_ui()


@inject
@dataclass
class SubjectContainer(
    AddObserverMixin,
    LocaleContainer[StyleT, ThemeT],
    ABC,
):
    """An abstract base class for a container of interactive widgets."""


@inject
@dataclass
class NavigableContainer(
    CreateNavButtonMixin,
    SubjectContainer[StyleT, ThemeT],
    ABC,
):
    """Abstract base class for navigation container."""
