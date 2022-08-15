"""
Games API /games endpoint.
"""
from flask import request
from flask_restx import Resource, fields, abort
from ..restplus import api
from models.sudoku import Sudoku
from loggings import get_module_logger

log = get_module_logger(__name__)

ns = api.namespace('games', description='Create, retrieve and update game')

DEFAULT_START_BOARD = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

# solution

# [8, 1, 2, 7, 5, 3, 6, 4, 9]
# [9, 4, 3, 6, 8, 2, 1, 7, 5]
# [6, 7, 5, 4, 9, 1, 2, 8, 3]
# [1, 5, 4, 2, 3, 7, 8, 9, 6]
# [3, 6, 9, 8, 4, 5, 7, 2, 1]
# [2, 8, 7, 1, 6, 9, 5, 3, 4]
# [5, 2, 1, 9, 7, 4, 3, 6, 8]
# [4, 3, 8, 5, 2, 6, 9, 1, 7]
# [7, 9, 6, 3, 1, 8, 4, 5, 2]

cell_erase_request_model = api.model(
    'CellEraseModel', {
        'row': fields.Integer(required=True,
                        description='The row number of the cell to be updated. This can only be between 0 - 8'),
        'column': fields.Integer(required=True, 
                        description='The column number of the cell to be updated. This can only be between 0 - 8'),
    })

cell_update_request_model = api.clone(
    'CellUpdateModel', cell_erase_request_model, {
        'value': fields.Integer(required=True,
                        description='The value to set the cell to. It can only be between 1 - 9'),
    })

game_response_model = api.model(
    'GameModel', {
        'board': fields.List(fields.List(fields.Integer), required=True,
                        description='2D array representing the sudoku board'),
        'game_win': fields.Boolean(required=True, description='Indicates if the game has been solved or not')
        
    })


@ns.route('/reset')
class GameResource(Resource):
    @ns.doc()
    @ns.marshal_with(game_response_model)
    def post(self):
        """Reset the board to the default state"""
        log.info(f'POST /games/reset')

        sudoku = Sudoku()

        try:
            sudoku.set_board(DEFAULT_START_BOARD)
        except Exception as e:
            log.exception(e)
            abort(400, f'Error while resetting the game - {str(e)}')

        return {'board': sudoku.get_board(), 'game_win': False}, 200

@ns.route('/cell/move')
class GameMoveResource(Resource):
    @ns.doc()
    @ns.expect(cell_update_request_model, validate=True)
    @ns.marshal_with(game_response_model)
    def post(self):
        """Make a move on the board by updating a cell with the passed value"""
        log.info(f'POST /games/cell/move')

        request_payload = request.get_json()

        value = int(request_payload['value'])
        if value < 1 or value > 9:
            abort(400, 'Value can only be between 1 to 9 inclusive')

        row = int(request_payload['row'])
        if row < 0 or row > 8:
            abort(400, 'Row can only be between 0 to 8 inclusive')

        column = int(request_payload['column'])
        if column < 0 or column > 8:
            abort(400, 'Column can only be between 0 to 8 inclusive')

        sudoku = Sudoku()

        if not sudoku.is_game_started():
            abort(400, 'Game is not started. Start the game before making a move')

        move_valid, message = sudoku.is_move_valid(row, column, value)
        if not move_valid:
            abort(400, message)

        try:
            sudoku.update_cell(row, column, value)
        except Exception as e:
            log.exception(e)
            abort(400, f'Error while making a move in the game - {str(e)}')

        return {'board': sudoku.get_board(), 'game_win': sudoku.is_board_passed()}, 200


@ns.route('/cell/erase')
class GameEraseResource(Resource):
    @ns.doc()
    @ns.expect(cell_erase_request_model, validate=True)
    @ns.marshal_with(game_response_model)
    def post(self):
        """
        Reset a cell on the board by setting the cell to 0
        if the cell is editable
        """
        log.info(f'POST /games/cell/erase')

        request_payload = request.get_json()

        row = int(request_payload['row'])
        if row < 0 or row > 8:
            abort(400, 'Row can only be between 0 to 8 inclusive')

        column = int(request_payload['column'])
        if column < 0 or column > 8:
            abort(400, 'Column can only be between 0 to 8 inclusive')

        sudoku = Sudoku()

        try:          
            sudoku.update_cell(row, column, 0)
        except Exception as e:
            log.exception(e)
            abort(400, f'Error while trying to reset the cell - {str(e)}')

        return {'board': sudoku.get_board(), 'game_win': sudoku.is_board_passed()}, 200

