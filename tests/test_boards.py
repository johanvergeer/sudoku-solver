import pytest

from soduku_solver.boards import SimpleBoard, Position


@pytest.fixture
def simple_board__4x4(board_4x4_1):
    return SimpleBoard(board_4x4_1)


def test_simple_board__init(simple_board__4x4, board_4x4_1):
    assert simple_board__4x4._board == board_4x4_1


def test_simple_board__set(simple_board__4x4):
    simple_board__4x4.set(Position(3, 0), 2)
    assert simple_board__4x4._board[0][3] == 2


def test_simple_board__get(simple_board__4x4):
    assert simple_board__4x4.get(Position(2, 0)) == 1


def test_simple_board__get_position_row(simple_board__4x4):
    assert simple_board__4x4.get_position_row(Position(3, 3)) == [0, 1, 4, 3]


def test_simple_board__get_position_column(simple_board__4x4):
    assert simple_board__4x4.get_position_column(Position(3, 3)) == [0, 0, 0, 3]


@pytest.mark.parametrize(
    "col,row,expected",
    [
        (0, 0, [3, 4, 0, 2]),
        (1, 1, [3, 4, 0, 2]),
        (3, 3, [2, 0, 4, 3]),
        (2, 2, [2, 0, 4, 3]),
        (2, 0, [1, 0, 0, 0]),
        (1, 2, [0, 0, 0, 1]),
    ]
)
def test_simple_board__get_position_sub_grid(simple_board__4x4, col, row, expected):
    assert simple_board__4x4.get_position_sub_grid(Position(col, row)) == expected


def test_simple_board__get_next_unresolved(simple_board__4x4):
    assert simple_board__4x4.get_next_unresolved() == Position(3, 0)


def test_simple_board__get_next_unresolved_2(simple_board__4x4):
    simple_board__4x4.set(Position(3, 0), 2)
    simple_board__4x4.set(Position(0, 1), 1)
    assert simple_board__4x4.get_next_unresolved() == Position(2, 1)


def test_simple_board__unset(simple_board__4x4):
    position_to_unset = Position(0, 0)
    simple_board__4x4.unset(position_to_unset)

    assert simple_board__4x4.get(position_to_unset) == 0
