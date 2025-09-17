"""Defines type vars."""

from typing import Literal, TypeVar

from wse.config.layout import BaseStyle, BaseThema

# Style types

StyleT = TypeVar('StyleT', bound=BaseStyle)
StyleT_co = TypeVar('StyleT_co', bound=BaseStyle, covariant=True)
ThemeT = TypeVar('ThemeT', bound=BaseThema)
ThemeT_co = TypeVar('ThemeT_co', bound=BaseThema, covariant=True)

# Observer pattern types

EntryT = TypeVar('EntryT')
ListenerT = TypeVar('ListenerT')
NotifyT = TypeVar('NotifyT', bound=str)
EntryNotifyT = Literal[
    'insert',
    'remove',
    'clear',
]
