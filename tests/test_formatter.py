import pytest

from soduku_solver.formatter import (
    create_simple_board_horizontal_separator,
    format_simple_board,
    format_simple_board_row,
)


@pytest.mark.parametrize(
    "row,formatted",
    [
        ([1, 2, 3, 4], "1 2 | 3 4"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], "1 2 3 | 4 5 6 | 7 8 9"),
    ],
)
def test_format_simple_board_row(row, formatted):
    assert format_simple_board_row(row) == formatted


@pytest.mark.parametrize(
    "size,separator", [(4, "- - + - -"), (9, "- - - + - - - + - - -"),]
)
def test_create_simple_board_horizontal_separator(size, separator):
    assert create_simple_board_horizontal_separator(size) == separator


def test_format_simple_board(simple_board__4x4):
    assert (
        format_simple_board(simple_board__4x4)
        == """3 4 | 1 0
0 2 | 0 0
- - + - -
0 0 | 2 0
0 1 | 4 3
"""
    )
