from flask import Flask, Blueprint

from api.restplus import api
from api.endpoints.health_check import ns as health_ns
from api.endpoints.game import ns as game_ns


MYNAME = 'sudoku'
app = Flask(MYNAME)

blueprint = Blueprint('api', MYNAME, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(health_ns)
api.add_namespace(game_ns)
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True)