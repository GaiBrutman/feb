"""
This module represents a binary view - a textual representation of the binary that can be
iterated over.
"""

from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Generator, Optional

from feb.core import Binary, Expression


class View(metaclass=ABCMeta):
    """
    The base class for code views.
    """

    def __init__(self, binary: Binary):
        self._binary: Binary = binary

    @property
    def binary(self):
        """
        The view binary object.
        """
        return self._binary

    @contextmanager
    def save_state(self):
        """
        Backs up the state of the view, restoring it when the context is done.
        """
        backup = self._binary.cursor
        yield self
        self._binary.cursor = backup

    @abstractmethod
    def get_expression(self) -> Optional[Expression]:
        """
        Get an expression at the current position, if available.
        This function should not change the cursor position.
        :return: An expression at the current position.
        """
        raise NotImplementedError()

    @abstractmethod
    def move(self, count: int):
        """
        Move the view by `count` expressions. Can move backwards.

        :param count: The number of expressions to move by.
        :raises IndexError: When the view cannot be moved by the requested count,
                            it will raise IndexError and will not change the cursor.
        """
        raise NotImplementedError()

    def walk(self, limit=None, reverse=False) -> Generator[Expression, None, None]:
        """
        Walk through the view's expressions. Either forward or backward.

        :param limit: (optional) The maximum number of expressions to yield.
        :type limit: _type_, optional
        :param reverse: Whether to walk backwards, defaults to False
        :yield: The next expression.
        """
        while limit is None or limit > 0:
            exp = self.get_expression()
            if exp is None:
                continue

            try:
                self.move(-1 if reverse else 1)
            except IndexError:
                break

            if limit is not None:
                limit -= 1
            yield exp
