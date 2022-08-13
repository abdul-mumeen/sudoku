import os
from flask import Flask, Blueprint
import werkzeug

# needed to do this because of open issue in Flask-restplus
werkzeug.cached_property = werkzeug.utils.cached_property

from api.restplus import api
from api.endpoints.health_check import ns as health_ns
from api.endpoints.game import ns as game_ns


MYNAME = 'sudoku'
app = Flask(MYNAME)
app.config['SECRET_KEY'] = 'secret!'

# manager = Manager(app=app)

blueprint = Blueprint('api', MYNAME, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(health_ns)
api.add_namespace(game_ns)
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True)