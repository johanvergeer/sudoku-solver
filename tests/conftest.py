import pytest

from soduku_solver.solver import Board


@pytest.fixture
def board_4x4_1() -> Board:
    return [
        [3, 4, 1, 0],
        [0, 2, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 4, 3],
    ]


@pytest.fixture
def board_4x4_1_solved() -> Board:
    return [
        [3, 4, 1, 2],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [2, 1, 4, 3],
    ]


@pytest.fixture
def board_9x9_1() -> Board:
    return [
        [6, 0, 5, 7, 2, 0, 0, 3, 9],
        [4, 0, 0, 0, 0, 5, 1, 0, 0],
        [0, 2, 0, 1, 0, 0, 0, 0, 4],
        [0, 9, 0, 0, 3, 0, 7, 0, 6],
        [1, 0, 0, 8, 0, 9, 0, 0, 5],
        [2, 0, 4, 0, 5, 0, 0, 8, 0],
        [8, 0, 0, 0, 0, 3, 0, 2, 0],
        [0, 0, 2, 9, 0, 0, 0, 0, 1],
        [3, 5, 0, 0, 6, 7, 4, 0, 8],
    ]
