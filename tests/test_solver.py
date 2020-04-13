from soduku_solver.boards import SimpleBoard
from soduku_solver.solver import solve


def test_solve__4x4(board_4x4_1, board_4x4_1_solved):
    board = SimpleBoard(board_4x4_1)
    solve(board)

    assert board._board == board_4x4_1_solved
