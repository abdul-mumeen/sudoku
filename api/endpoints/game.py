"""
Games API /games endpoint.
"""
import logging
from datetime import datetime
from flask import request
from flask_restx import Resource, fields, abort
from ..restplus import api
from services.sudoku import Sudoku

log = logging.getLogger(__name__)

ns = api.namespace('games', description='Create, retrieve and update game')

DEFAULT_START_BOARD = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,8,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


game_response_model = api.model(
    'GameModel', {
        'board':
        fields.List(fields.List(fields.Integer),required=True,
                      description='2D array representing the sudoku board')
    })


@ns.route('/reset')
class GameResource(Resource):
    @ns.doc()
    @ns.expect(game_response_model)
    def post(self):
        """Reset the board to the default state"""
        log.info(f'POST /games/reset')

        sudoku = Sudoku()

        try:
            sudoku.set_board(DEFAULT_START_BOARD)
        except Exception as e:
            log.exception(e)
            abort(404, f'Error while resetting the game - {str(e)}')

        return {'board': sudoku.board}, 200

