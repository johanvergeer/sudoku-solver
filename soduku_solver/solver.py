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


def print_board(bo: Board):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
