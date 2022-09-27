"""
Tests the Cursor logic
"""

from feb.core import Cursor, RebasedCursor


def test_add():
    """
    Test adding values to a cursor.
    """
    cases = [
        ((1, 2), 3),
        ((-5, 2), -3),
    ]

    for (a, b), c in cases:
        cursor = Cursor(a) + b
        assert isinstance(cursor, Cursor)
        assert cursor == c


def test_sub():
    """
    Test subtracting values from a cursor.
    """
    cases = [
        ((1, 2), -1),
        ((-5, 2), -7),
    ]

    for (a, b), c in cases:
        cursor = Cursor(a) - b
        assert isinstance(cursor, Cursor)
        assert cursor == c


def test_cursor_sub():
    """
    Test subtracting a cursor from a cursor.
    """
    cases = [
        ((1, 2), -1),
        ((-5, 2), -7),
    ]

    for (a, b), c in cases:
        cursor = Cursor(a) - Cursor(b)
        assert isinstance(cursor, Cursor)
        assert cursor == c


def test_isub():
    """
    Test inline subtracting values from a cursor.
    """
    cases = [
        ((1, 2), -1),
        ((-5, 2), -7),
    ]

    for (a, b), c in cases:
        cursor = Cursor(a)
        cursor -= b
        assert isinstance(cursor, Cursor)
        assert cursor == c


def test_cursor_isub():
    """
    Test inline subtracting a cursor from a cursor.
    """
    cases = [
        ((1, 2), -1),
        ((-5, 2), -7),
    ]

    for (a, b), c in cases:
        cursor = Cursor(a)
        cursor -= Cursor(b)
        assert isinstance(cursor, Cursor)
        assert cursor == c


def test_init_from_another_cursor():
    """
    Test cursor initialization from another cursor.
    """
    cursor1 = Cursor(10)
    cursor2 = Cursor(cursor1)
    assert cursor1.value == cursor2.value
    assert isinstance(cursor1.value, int)
    assert isinstance(cursor2.value, int)


def test_rebased_cursor():
    """
    Test the RebasedCursor logic.
    """
    base = 10
    cursor = Cursor(2)
    rebased_cursor = RebasedCursor(cursor, base=base)
    assert cursor.value == 2
    assert rebased_cursor.value == base + 2

    cursor.value = 5
    assert cursor.value == 5
    assert rebased_cursor.value == base + 5

    rebased_cursor.value = base + 3
    assert cursor.value == 3
    assert rebased_cursor.value == base + 3


def test_change_rebased_cursor_base():
    """
    Test the RebasedCursor during a base change.
    """
    base = 10
    cursor = Cursor(2)
    rebased_cursor = RebasedCursor(cursor, base=base)
    assert cursor.value == 2
    assert rebased_cursor.value == base + 2

    new_base = 12
    rebased_cursor.base = new_base
    assert cursor.value == 2
    assert rebased_cursor.value == new_base + 2
