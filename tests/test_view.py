"""
Tests for the View class
"""

import pytest
from feb.core import Binary, Expression, View


def clamp(num, minimum, maximum):
    """
    Clamp a number to specified limits.

    :param num: The number to clamp.
    :param minimum: The minimum limit.
    :param maxi: The maximum limit.
    :return: The clamped result.
    """
    return max(min(maximum, num), minimum)


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


class ListView(View):
    """
    A dummy view for testing, iterates over a list.
    """

    def __init__(self, binary, lst):
        super().__init__(binary)
        self._list = lst

    def _is_in_list_range(self):
        return 0 <= self.binary.cursor < len(self._list)

    def get_expression(self):
        """
        Gets the current list expression, if available.
        :return: the current expression, or None if out-of-range or if element is None.
        """
        if not self._is_in_list_range():
            return None
        element = self._list[self.binary.cursor.value]
        if element is None:
            return None
        return DummyExpression(str(element))

    def move(self, count: int):
        """
        Move the view cursor by a given count.

        :param count: The number of expression to move by.
        :raises IndexError: If gone out of range.
        """
        # Clamp the cursor to the list limits, to recover from out-of-bound moves.
        self.binary.cursor = clamp(self.binary.cursor, -1, len(self._list))

        self.binary.cursor += count
        if not self._is_in_list_range():
            raise IndexError()


@pytest.fixture(scope="function")
def binary():
    """
    A dummy binary object fixture
    """
    return Binary(__file__)


def test_view_walk(binary):
    """
    Test the View.walk() method
    """
    nums = list(range(5))
    view = ListView(binary, nums)
    for i, expr in enumerate(view.walk(limit=5)):
        assert expr.text == str(nums[i])

    # Test walking backwards to start
    for i, expr in enumerate(view.walk(limit=5, reverse=True)):
        assert expr.text == str(nums[len(nums) - i - 1])


def test_view_walk_past_limit(binary):
    """
    Test walking through a view past it's limits (from start and end)
    """
    nums = list(range(5))
    view = ListView(binary, nums)

    assert len(list(view.walk(limit=5))) == 5
    assert view.binary.cursor == 5  # Gone out of bounds
    assert not list(view.walk(limit=5))
    assert not list(view.walk())

    assert len(list(view.walk(limit=5, reverse=True))) == 5
    assert view.binary.cursor == -1
    assert not list(view.walk(limit=5, reverse=True))
    assert not list(view.walk(reverse=True))


@pytest.mark.timeout(0.5)
def test_view_walk_skips_invalid_data(binary):
    """
    Test walking over a list with invalid elements that yield None.
    """
    view = ListView(binary, [None] + list(range(4)))
    assert len(list(view.walk(limit=5))) == 4
