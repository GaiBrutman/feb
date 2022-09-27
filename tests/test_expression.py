"""
Tests the Operand and Expressions classes
"""

from typing import Iterable
from feb.core import Expression, Operand


class DummyOperand(Operand):
    """
    A dummy operand class for testing.
    :type Operand: _type_
    """

    def __init__(self, line, start, stop):
        self._line = line
        self._start = start
        self._stop = stop

    @property
    def line(self):
        return self._line

    @property
    def slice(self):
        return slice(self._start, self._stop)


class DummyExpressions(Expression):
    """
    Dummy class for an expression of words
    """

    def __init__(self, words):
        self._words = words

    @property
    def text(self):
        return " ".join(self._words)

    def get_operands(self) -> Iterable[Operand]:
        idx = 0
        operands = []
        for word in self._words:
            operands.append(DummyOperand(self.text, idx, idx + len(word)))
            idx += len(word) + 1  # With space
        return operands


def test_operand_get_text():
    """
    Tests Operand.get_text() method
    """
    operand = DummyOperand("hello", 1, 3)
    assert operand.get_text() == "hello"[1:3]


def test_expression_operands():
    """
    Test Operand.get_text() when getting operands from a dummy expression.
    """
    words = ["hello", "world"]
    exp = DummyExpressions(words)
    operands = exp.get_operands()

    for operand in operands:
        assert operand.line == exp.text
    assert [operand.get_text() for operand in operands] == words
