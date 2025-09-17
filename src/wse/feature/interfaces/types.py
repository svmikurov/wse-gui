"""Defines type vars."""

from typing import TypeVar

from mypy.types import TypedDictType

from wse.config.layout import BaseStyle, BaseThema

StyleT = TypeVar('StyleT', bound=BaseStyle)
StyleT_co = TypeVar('StyleT_co', bound=BaseStyle, covariant=True)

ThemeT = TypeVar('ThemeT', bound=BaseThema)
ThemeT_co = TypeVar('ThemeT_co', bound=BaseThema, covariant=True)

NotifyT = TypeVar('NotifyT', bound=str)
ListenerT = TypeVar('ListenerT')

TypedDictT = TypeVar('TypedDictT', bound=TypedDictType)
