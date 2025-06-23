Type checking
=============

Using `@runtime_checkable`
--------------------------

The project uses the "injector" library. The Injector library uses runtime checking.
This is why the @runtime_checkable decorator is sometimes
added to protocol interfaces used with the "injector" library.