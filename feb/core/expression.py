"""
This module hold the logic for accessing the binary information - through Expressions and Operands.
"""

from abc import ABCMeta, abstractmethod
from typing import Iterable


class Operand(metaclass=ABCMeta):
    """
    An Operand inside an Expression. Used to extract different values from the expression.
    """

    @property
    @abstractmethod
    def line(self) -> str:
        """
        The whole line that contains the operand.
        :return: The line that contains the operand;
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def slice(self) -> slice:
        """
        The range of the operand text inside of the whole line.
        :return: A slice object to slice the operand line.
        """
        raise NotImplementedError()

    def get_text(self) -> str:
        """
        Gets the text of the operand from it's line.
        :return: The text of the operand.
        """
        return self.line[self.slice]


class Expression(metaclass=ABCMeta):
    """
    A code expression. An expression can hold operands that can be extracted from it.
    """

    @property
    @abstractmethod
    def text(self):
        """
        The textual representation of the expression.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_operands(self) -> Iterable[Operand]:
        """
        Gets the operands of the expression.
        :return: An iterable of the operands of the expression.
        """
        raise NotImplementedError()

    def __repr__(self):
        return self.text
