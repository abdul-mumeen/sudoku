import unittest

from app import app
from models.cell import Cell
from models.sudoku import Sudoku

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_cell_model(self):
        cell = Cell(5, True)
        
        value = cell.cell_value()
        self.assertEqual(5, value)

        cell.set_cell_value(20)
        value = cell.cell_value()
        self.assertEqual(20, value)

    def test_sudoku_model_initialization(self):
        sudoku = Sudoku()
        self.assertEqual([], sudoku.get_board())


if __name__ == "__main__":
    unittest.main()