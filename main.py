# import flask.scaffold
# flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
# from flask_restx import Api
# from src.models import db
# # from src.resources import socketio, notifikasi
# from src.resources import root

# from flask import Flask
# from flask_cors import CORS
# from config import get_config


# # from src.event import socketio

# # app = Flask(__name__, static_folder='static')
# # app.config.from_object(get_config(None))
# # db.init_app(app)
# def create_app(env=None):
#     app = Flask(__name__, static_folder='static')
#     cors = CORS(app, resources={r"/*": {"origins": "*"}})
#     app.config.from_object(get_config(env))

#     db.init_app(app)
    
#     return app
# app = create_app()

# # socketio.init_app(app, cors_allowed_origins="*", logger=True, engineio_logger=True, debug=True, async_mode="eventlet")


# # socket = socketio.init_app(app, logger=True, engineio_logger=True, cors_allowed_origins="*")

# # API
# api = Api(app,title='FLASK TEST', description="flask test", validate=True)

# api.add_namespace(root)



from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify

app = Flask(__name__)
CORS(app, supports_credentials=True)
sslify = SSLify(app)

@app.route("/")
def index():
    return "Hello World!"