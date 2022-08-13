"""
This module implements the binary cursor interfaces.
"""

from functools import total_ordering


def param_into_value(func):
    def inner(self, other):
        if isinstance(other, Cursor):
            other = other.value
        return func(self, other)

    return inner


@total_ordering
class Cursor:
    """
    A Cursor represents the current offset inside a binary.
    """

    def __init__(self, value=0):
        self.value = value

    @property
    def value(self) -> int:
        """
        The inner cursor value.
        """
        return self._value

    @value.setter
    def value(self, value):
        self._value = value.value if isinstance(value, Cursor) else int(value)

    @param_into_value
    def __add__(self, other) -> "Cursor":
        if isinstance(other, Cursor):
            other = other.value
        return Cursor(self.value + other)

    @param_into_value
    def __iadd__(self, other) -> "Cursor":
        if isinstance(other, Cursor):
            other = other.value
        return Cursor(self.value + other)

    @param_into_value
    def __sub__(self, other) -> "Cursor":
        if isinstance(other, Cursor):
            other = other.value
        return Cursor(self.value - other)

    @param_into_value
    def __isub__(self, other) -> "Cursor":
        if isinstance(other, Cursor):
            other = other.value
        return Cursor(self.value - other)

    @param_into_value
    def __eq__(self, other):
        return self.value == other

    @param_into_value
    def __lt__(self, other):
        return self.value < other

    def __repr__(self):
        return f"Cursor({self.value.__repr__()})"


class RebasedCursor(Cursor):
    """
    A cursor rebased to an inner cursor value
    """

    def __init__(self, cursor: Cursor, base):
        """
        Initialize a RebasedCursor.

        :param cursor: The inner cursor reference to follow.
        :param base: The baseline to rebase the inner cursor values to.
        """
        self._inner = cursor
        self.base = base
        super().__init__(base + cursor.value)

    @property
    def value(self):
        return self.base + self._inner.value

    @value.setter
    def value(self, value):
        self._inner.value = value - self.base
