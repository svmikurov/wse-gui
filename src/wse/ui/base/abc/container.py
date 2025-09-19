"""Defines abstract base class for widget containers."""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

from wse.core.exceptions import PopulateContentError
from wse.feature import StyleT, ThemeT
from wse.feature.base.abstract.ui_layer import LocalizeABC, UpdateStyleABC
from wse.feature.base.mixins import GetContentMixin

logger = logging.getLogger(__name__)


@dataclass
class AddContentABC(
    GetContentMixin,
    ABC,
):
    """Abstract base class for widget container."""

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._setup()

        try:
            self._populate_content()
        except AttributeError as err:
            logger.exception(PopulateContentError(err))
        except Exception:
            logger.exception('Unexpected populate content error:\n')

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


class ContainerABC(
    UpdateStyleABC[StyleT, ThemeT],
    AddContentABC,
    LocalizeABC,
    ABC,
):
    """ABC for container."""

    def _setup(self) -> None:
        super()._setup()
        self.localize_ui()
        self._apply_styles()
