Know problems
=============

Empty screen
------------

Problem: An empty screen is displayed

Possible reason: Not called ``super().__post_init__()`` of View inherited from ``ViewABC``

Troubleshooting: Add ``super().__post_init__()``

.. code-block:: python
   :caption: Check that the **super** method was called.

   class SomeView(..., ViewABC, ...):

       def __post_init__(self) -> None:
           ...
           super().__post_init__()
           ...

No functionality
----------------

Problem: Method of class not calls

Possible reason: Class not decorated with ``@inject`` and / or with ``@dataclass``

Troubleshooting: Decorate class with ``@inject`` and / or with ``@dataclass``

.. code-block:: python

   @inject
   @dataclass
   class Some: ...
