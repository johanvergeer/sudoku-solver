import os
from math import sqrt

from soduku_solver.boards import Combination, SimpleBoard


def format_simple_board(board: SimpleBoard):
    formatted = ""
    block_size = int(sqrt(board.size))
    separator = create_simple_board_horizontal_separator(board.size)

    for index, row in enumerate(board):
        formatted += format_simple_board_row(row) + os.linesep

        if index % block_size and index + 1 != board.size:
            formatted += separator + os.linesep

    return formatted


def format_simple_board_row(row: Combination) -> str:
    formatted = ""
    block_size = int(sqrt(len(row)))
    for index, value in enumerate(row):
        formatted += f"{value} "
        if (index + 1) % block_size == 0 and index + 1 != len(row):
            formatted += "| "

    return formatted[:-1]


def create_simple_board_horizontal_separator(size: int) -> str:
    formatted = ""
    block_size = int(sqrt(size))

    for col in range(1, size + 1):
        formatted += "- "
        if col % block_size == 0:
            formatted += "+ "

    return formatted[:-3]
