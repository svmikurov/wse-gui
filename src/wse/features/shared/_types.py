"""Defines type vars."""

from typing import TypeVar

from wse.config.layout import BaseStyle, BaseThema

StyleT = TypeVar('StyleT', bound=BaseStyle)
ThemeT = TypeVar('ThemeT', bound=BaseThema)
