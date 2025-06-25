"""Features interfaces."""

__all__ = [
    'IAddObserver',
    'IContainer',
    'IContent',
    'IController',
    'IGetContent',
    'IModel',
    'IObserver',
    'ISubject',
    'IView',
]

from .icontainer import IContainer
from .icontent import IContent, IGetContent
from .imvc import IController, IModel, IView
from .iobserver import IAddObserver, IObserver, ISubject
