class SudokuMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        This ensures that possible changes to the value of the `__init__` 
        argument do not affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Sudoku(metaclass=SudokuMeta):
    def __init__(self):
        self.board = []

    def set_board(self, new_board):
        self.board = new_board

    def move(self, row, column, value):
        pass

    def is_move_valid(self, row, column, value):
        pass

    def is_board_passed(self):
        pass