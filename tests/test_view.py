"""
Tests for the View class
"""

from feb.core import Binary, Expression, View


class DummyExpression(Expression):
    """
    Dummy class for an Expression
    """

    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text

    def get_operands(self):
        return []


class DummyView(View):
    """
    Dummy view for testing.
    """

    def __init__(self, binary, limit):
        super().__init__(binary)
        self.limit = limit

    def get_expression(self):
        return DummyExpression(str(self.binary.cursor.value))

    def move(self, count: int):
        index = self.binary.cursor.value + (count * 2)
        print(f"moving from {self.binary.cursor.value} to {index}")
        if not 0 <= index <= self.limit * 2:
            print("raise")
            raise IndexError()
        self.binary.cursor = index


def test_view_walk():
    """
    Test the View.walk() method
    """

    binary = Binary(__file__)
    view = DummyView(binary, 5)
    for i, expr in enumerate(view.walk(limit=5)):
        assert expr.text == str(i * 2)

    # Test walking backwards to start
    for i, expr in enumerate(view.walk(limit=5, reverse=True)):
        assert expr.text == str(10 - (i * 2))


def test_view_walk_past_limit():
    """
    Test walking through a view past it's limits (from start and end)
    """
    binary = Binary(__file__)
    view = DummyView(binary, 5)
    assert len(list(view.walk(limit=5))) == 5
    assert binary.cursor == 10
    assert not list(view.walk(limit=5))
    assert not list(view.walk())

    assert len(list(view.walk(limit=5, reverse=True))) == 5
    assert not list(view.walk(limit=5, reverse=True))
    assert not list(view.walk(reverse=True))
