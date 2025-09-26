"""Defines type vars."""

from typing import Literal, TypeVar

from wse.config.layout import BaseStyle, BaseTheme

# Style types

StyleT = TypeVar('StyleT', bound=BaseStyle)
ThemeT = TypeVar('ThemeT', bound=BaseTheme)

# Observer pattern types

ListenerT = TypeVar('ListenerT')  # For Source listener
ObserverT = TypeVar('ObserverT')  # For Subject observer
NotifyT = TypeVar('NotifyT', bound=str)
AccessorT = TypeVar('AccessorT', bound=str)

# Entry (Data-Transfer-Object)

EntryT = TypeVar('EntryT')
EntryNotifyT = Literal[
    'insert',
    'remove',
    'clear',
]
