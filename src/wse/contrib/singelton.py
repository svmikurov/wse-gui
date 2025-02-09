"""Singleton base class."""


class Singleton:
    """Moving to page the button controller."""

    __instance = None

    def __new__(cls) -> None:
        """Create single instance."""
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        """Construct the navigation."""
        pass

    def __del__(self) -> None:
        """Delete the class instance."""
        self.__class__.__instance = None
