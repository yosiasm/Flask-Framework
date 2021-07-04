import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restx import Api
from src.models import db_sql, UserModel
from src.resources import user
# from src.resources import socketio, notifikasi

from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS
from config import get_config


# from src.event import socketio

# app = Flask(__name__, static_folder='static')
# app.config.from_object(get_config(None))
# db.init_app(app)
def create_app(env=None):
    app = Flask(__name__, static_folder='static')
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(get_config(env))

    db_sql.init_app(app)
    
    return app
app = create_app()
Migrate(app, db_sql)

# socketio.init_app(app, cors_allowed_origins="*", logger=True, engineio_logger=True, debug=True, async_mode="eventlet")

# API
api = Api(app,title='FLASK TEST', description="flask test", validate=True)

api.add_namespace(user)

# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db_sql, User=UserModel)




# from flask import Flask

# app = Flask(__name__,ssl_context='adhoc')

# @app.route("/")
# def index():
#     return "Hello World!"