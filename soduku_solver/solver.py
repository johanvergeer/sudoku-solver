from soduku_solver.boards import Board


def solve(board: Board) -> bool:
    pos = board.get_next_unresolved()
    if not pos:
        # Last field is resolved
        return True

    for num in board.get_available_numbers(pos):
        board.set(pos, num)

        if solve(board):
            return True

        board.unset(pos)

    return False
