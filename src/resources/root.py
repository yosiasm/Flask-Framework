from flask import request, jsonify, make_response
from flask_restx import Namespace, Resource, fields
# from ..repositories import NotifikasiRepository as Repository #change this

resource_name = "root" #change this
resource_title = resource_name.replace('-',' ').title()
api = Namespace(resource_name, description=f'{resource_title} related operations')

@api.route('/')
class Root(Resource):    

    def get(self):
        return {"message":"API is running"},200
