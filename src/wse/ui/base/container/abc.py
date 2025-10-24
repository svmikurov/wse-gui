"""Defines abstract base class for widget containers."""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic

from wse.core.exceptions import PopulateContentError
from wse.feature import StyleT, ThemeT
from wse.ui.base.content.mixins import GetContentMixin

from .abc_locale import LocalizeABC
from .abc_style import UpdateStyleGenABC

log = logging.getLogger(__name__)


class ContainerABC(ABC):
    """ABC for container."""

    @abstractmethod
    def _create_ui(self) -> None: ...

    @abstractmethod
    def _populate_content(self) -> None: ...


class ApplyStyleGenABC(ABC, Generic[StyleT, ThemeT]):
    """ABC to apply style."""

    _style: StyleT
    _theme: ThemeT

    @abstractmethod
    def update_style(self, config: StyleT | ThemeT) -> None:
        """Update widgets style."""


# **DEPRECATED** use above


@dataclass
class CreateContentABC(
    GetContentMixin,
    ABC,
):
    """ABC for create content."""

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._setup()

        try:
            self._populate_content()
        except AttributeError as err:
            log.exception(PopulateContentError(err))
        except Exception:
            log.exception('Unexpected populate content error:\n')

    def _setup(self) -> None:  # noqa: B027
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
class ContainerGenABC(
    UpdateStyleGenABC[StyleT, ThemeT],
    CreateContentABC,
    LocalizeABC,
    ABC,
    Generic[StyleT, ThemeT],
):
    """ABC for container."""

    def _setup(self) -> None:
        super()._setup()
        self.localize_ui()
        self._apply_styles()
