from soduku_solver.solver import find_empty


def test_find_empty(board_4x4_1):
    assert find_empty(board_4x4_1) == (0, 3)


def test_find_empty__already_solved(board_4x4_1_solved):
    assert find_empty(board_4x4_1_solved) is None
