"""
This module holds the Binary class, which represents an open binary state.
"""
from feb.core import Cursor


class Binary:
    """
    The Binary class represents an open binary.
    It holds global information about the binary, it's entry and current cursor for example.
    """

    def __init__(self, name, entry=0):
        self.name = name
        self._entry_address = entry
        self._cursor: Cursor = self.entry

    @property
    def entry(self):
        """
        A cursor of the binary entry point. Does not change.
        :return: A Cursor object of the binary entry point.
        """
        return Cursor(self._entry_address)

    @property
    def cursor(self) -> Cursor:
        """
        The current offset of the explored binary (in bytes).
        :return: A cursor object of the binary current location.
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        """
        Sets the cursor *value*.
        Does not change the cursor reference to allow use of RebasedCursor().
        """
        self._cursor.value = Cursor(value)

    def __repr__(self):
        return f"{self.name}@{self.cursor.value}"
