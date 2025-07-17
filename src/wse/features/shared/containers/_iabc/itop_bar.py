"""Defines abc and protocols for the container interface."""

from abc import ABC
from typing import Protocol

from wse.config.layout import TopBarStyle, TopBarTheme
from wse.features.base import BaseController
from wse.features.base.container import NavigableContainerABC
from wse.features.base.mixins import AddObserverMixin, NotifyNavigateMixin
from wse.features.interfaces.icontainer import (
    IAddObserver,
    INavigableContainer,
)
from wse.features.interfaces.icontent import IGetContent


class ITopBarContainer(
    INavigableContainer[TopBarStyle, TopBarTheme],
    Protocol,
):
    """Protocol for Top Bar container interface."""


class ITopBarController(
    IAddObserver,
    IGetContent,
    Protocol,
):
    """Protocol for Top Bar controller interface."""


class BaseTopBarContainer(
    NavigableContainerABC[TopBarStyle, TopBarTheme],
    ABC,
):
    """Base class for Top Bar container."""


class BaseTopBarController(
    AddObserverMixin,
    NotifyNavigateMixin,
    BaseController,
    ABC,
):
    """Base class for Top bar controller."""
