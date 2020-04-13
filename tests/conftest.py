from typing import List

import pytest

from soduku_solver.boards import SimpleBoard


@pytest.fixture
def simple_board__4x4(board_4x4_1):
    return SimpleBoard(board_4x4_1)


@pytest.fixture
def board_4x4_1() -> List[List[int]]:
    return [
        [3, 4, 1, 0],
        [0, 2, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 4, 3],
    ]


@pytest.fixture
def board_4x4_1_solved() -> List[List[int]]:
    return [
        [3, 4, 1, 2],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [2, 1, 4, 3],
    ]


@pytest.fixture
def board_9x9_1() -> List[List[int]]:
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
