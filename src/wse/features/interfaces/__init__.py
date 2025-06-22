"""Features interfaces."""

__all__ = [
    'IContent',
    'IController',
    'IObserver',
    'ISubject',
    'IView',
]

from .icontent import IContent
from .imvc import IController, IView
from .iobserver import IObserver, ISubject
