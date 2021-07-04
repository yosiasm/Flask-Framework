from flask import request
from flask.helpers import make_response
from flask_restx import Namespace, Resource, fields
from src.repositories import UserRepository as Repository #change this
import os

resource_name = "user" #change this
resource_title = resource_name.replace('-',' ').title()
api = Namespace(resource_name, description=f'{resource_title} related operations')

api_field = api.model(resource_title, { #change this
    'place_of_birth': fields.String(required=False, description=f'place_of_birth {resource_name}'),
    'date_of_birth': fields.String(required=False, description=f'date_of_birth {resource_name}'),
    'phone': fields.String(required=False, description=f'phone {resource_name}'),
    'home_address': fields.String(required=False, description=f'home_address {resource_name}'),
    'email': fields.String(required=True, description=f'email {resource_name}'),
    'first_name': fields.String(required=True, description=f'first_name {resource_name}'),
    'last_name': fields.String(required=True, description=f'last_name {resource_name}'),
    'password': fields.String(required=True, description=f'password {resource_name}'),
    'is_admin': fields.String(required=True, description=f'is_admin {resource_name}'),

    'is_active' : fields.Boolean(required=True, description=f'is_active for {resource_name}'),
    'is_delete' : fields.Boolean(required=False, description=f'is_delete for {resource_name}', default=False),
    'created_by' : fields.String(required=False, description=f'created_by for {resource_name}')
})

@api.route('')
class Module(Resource): #change this
    @api.doc(params={'page': 'Page ', 'pageSize': 'Size data per page', 'is_delete': 'Filter Delete data'})
    def get(self):
        data_list = Repository.list(request)
        return data_list, data_list['code']

    @api.expect(api_field)
    def post(self):
        data_create = Repository.create(request)
        return data_create, data_create['code']

@api.route('/<id>')
class ModuleWithId(Resource):    
    @api.expect(api_field)
    def put(self, id):        
        data_update = Repository.edit(id, request)
        return data_update, data_update['code']
    
    def get(self, id):
        data_show = Repository.show(id)
        return data_show, data_show['code']

    def delete(self, id):
        data_delete = Repository.remove(id)
        return data_delete, data_delete['code']

