"""
flask-restplus specific initializations.
"""
from flask_restx import Api

api = Api(version='1', title='Sudoku', description='Have fun with sudoku game')


@api.errorhandler
def default_error_handler(err):
    message = 'An unhandled exception occurred: {}'.format(err)
    # Flask capture any uncaught errors and log them.

    return {'message': message}, 500