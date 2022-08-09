"""
flask-restplus specific initializations.
"""
import logging

from flask_restx import Api

log = logging.getLogger(__name__)

api = Api(version='1', title='Sudoku', description='Have fun with sudoku game')


@api.errorhandler
def default_error_handler(err):
    message = 'An unhandled exception occurred: {}'.format(err)
    # Flask capture any uncaught errors and log them.

    return {'message': message}, 500