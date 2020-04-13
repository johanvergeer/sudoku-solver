from abc import abstractmethod
from dataclasses import dataclass
from math import sqrt
from typing import Iterable, Iterator, List, Optional, Set

from typing_extensions import Protocol

Combination = List[int]
"""Row, Column or Sub grid"""


@dataclass
class Position:
    """The column and row pos on the Sudoku board"""

    column: int
    row: int


class Board(Protocol):
    @abstractmethod
    def set(self, position: Position, value: int) -> None:
        ...

    @abstractmethod
    def unset(self, position: Position) -> None:
        ...

    @abstractmethod
    def get(self, position: Position) -> int:
        ...

    @abstractmethod
    def get_next_unresolved(self) -> Position:
        ...

    @property
    @abstractmethod
    def size(self) -> int:
        ...

    @abstractmethod
    def get_available_numbers(self, position: Position) -> Set[int]:
        ...


class SimpleBoard(Board, Iterable):
    def __iter__(self) -> Iterator[Combination]:
        for row in self._board:
            yield row

    def __init__(self, board: List[List[int]]):
        self._board = board

    def set(self, position: Position, value: int) -> None:
        self._board[position.row][position.column] = value

    def unset(self, position: Position) -> None:
        self._board[position.row][position.column] = 0

    def get(self, position: Position) -> int:
        return self._board[position.row][position.column]

    def get_position_row(self, position: Position) -> Combination:
        return self._board[position.row]

    def get_position_column(self, position: Position) -> Combination:
        return [row[position.column] for row in self._board]

    def get_position_sub_grid(self, position: Position) -> Combination:
        size = int(sqrt(self.size))  # Sub grid width
        box_x = position.column // size
        box_y = position.row // size

        combination = []

        for i in range(box_y * size, box_y * size + size):
            for j in range(box_x * size, box_x * size + size):
                combination.append(self._board[i][j])

        return combination

    def get_next_unresolved(self) -> Optional[Position]:
        size = len(self._board)
        for row in range(size):
            for column in range(size):
                position = Position(column, row)
                if self.get(position) == 0:
                    return position
        return None

    @property
    def size(self) -> int:
        return len(self._board)

    def get_available_numbers(self, position: Position) -> Set[int]:
        full_set = set(range(1, self.size + 1))
        in_use = set(
            self.get_position_row(position)
            + self.get_position_column(position)
            + self.get_position_sub_grid(position)
        )

        return full_set.difference(in_use)
