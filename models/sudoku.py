from __future__ import annotations
from typing import Tuple
from loggings import get_module_logger
from .cell import Cell
from .singleton import SudokuMeta

log = get_module_logger(__name__)

class Sudoku(metaclass=SudokuMeta):
    def __init__(self) -> None:
        """Initialize the board"""
        self.board = []

    def is_empty_cell(self) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j].value == 0:
                    return True
        return False

    def set_board(self, new_board) -> None:
        """Set the board to the value of the 2D array of intergers received"""

        board = []
        for i in range(len(new_board)):
            row = []
            for j in range(len(new_board[0])):
                value = new_board[i][j]
                is_editable = True if value == 0 else False
                new_cell = Cell(value, is_editable)
                row.append(new_cell)
            board.append(row)
        self.board = board

    def get_board(self) -> list:
        """Return the board as a nested list of integers"""
        board = []
        for i in range(len(self.board)):
            row = []
            for j in range(len(self.board[0])):
                row.append(self.board[i][j].value)
            board.append(row)
        
        return board

    def update_cell(self, row, column, value) -> None:
        """
        Update a cell with the value if the cell is editable.
        This means, not part of the default values on the board
        """
        if not self.board[row][column].is_editable:
            raise Exception('Cell is not editable')
        self.board[row][column].set_cell_value(value)

    def is_move_valid(self, row, column, value) -> Tuple[bool, str]:
        """
        Check that cell is not filled and there is no already existing duplicate value
        on the row, column and immediate boxof the value supplied
        """
        # Check that cell does not have a value
        if self.board[row][column].value != 0:
            return False, 'Invalid move, cell has a value, erase it first'

        # Check duplicate in box
        box_row_start = (row // 3) * 3
        box_row_end = box_row_start + 3
        box_column_start = (column // 3) * 3
        box_column_end = box_column_start + 3

        for i in range(box_row_start, box_row_end):
            for j in range(box_column_start, box_column_end):
                if self.board[i][j].value == value and not (i == row and j == column):
                    return False, 'Invalid move, duplicate number in the same box'

        # Check duplicate in column
        for i in range(len(self.board[0])):
            if self.board[i][column].value == value and row != i:
                return False, 'Invalid move, duplicate number on the same column'

        # Check duplicate in row
        for i in range(len(self.board)):
            if self.board[row][i].value == value and column != i:
                return False, 'Invalid move, duplicate number on the same row'

        return True, ''

    def is_board_passed(self) -> bool:
        """The game is completed when there are no empty cells"""
        return not self.is_empty_cell()

    def is_game_started(self) -> bool:
        """The game is started when the board is not an empty list"""
        if self.board:
            return True
        return False