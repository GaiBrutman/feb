"""
Tests of Binary class
"""

from feb.core import Binary, Cursor


def test_init():
    """
    Tests the initialization of a Binary object.
    """
    binary = Binary(__file__)
    assert binary.entry == binary.cursor == Cursor(0)
    assert str(binary) == f"{__file__}@{0}"


def test_change_cursor():
    """
    Tests the binary cursor change logic.
    """
    binary = Binary(__file__)
    # The cursor reference does not change. We need to copy.
    cursor = Cursor(binary.cursor.value)

    binary.cursor += 5
    assert binary.cursor == cursor + 5
    assert binary.entry == cursor

    binary.cursor = 6
    assert binary.cursor == 6
    assert binary.entry == cursor
