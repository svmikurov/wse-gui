"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

from wse.features.interfaces import IController, IView


class ISimpleCalcView(IView, Protocol):
    """The view of Simple Math calculation page."""


class ISimpleCalcController(IController, Protocol):
    """The controller of Simple Math calculation page."""
