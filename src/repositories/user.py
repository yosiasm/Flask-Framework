from sqlalchemy.exc import IntegrityError
from src.models import UserModel as Model #change this
from src.models.user import User as Field #change this
from utils import BuildResponse, list_default_param
import datetime

repo_name = 'User' #change this

def create_doc(field:Field): #change this
    doc = {
        'id': str(field.id),
        'place_of_birth': field.place_of_birth,
        'date_of_birth': str(field.date_of_birth),
        'phone': field.phone,
        'home_address': field.home_address,
        'email': field.email,
        'first_name': field.first_name,
        'last_name': field.last_name,
        'password': field.password,
        'is_admin': field.is_admin,
        'is_active': field.is_active,
        'is_delete': field.is_delete,
        'created_at': field.created_at,
        'updated_at': field.updated_at,
        'created_by': str(field.created_by), 
    } 
    return doc

class UserRepository: #change this
    @staticmethod
    def list(request):
        try:
            page, pageSize, is_delete = list_default_param(request)

            rows = Model.query.filter_by(is_delete=is_delete)

            len_fields = rows.count()

            fields = rows.paginate(page=page, per_page=pageSize, error_out=False).items
            data = {}
            data = [create_doc(row) for row in fields]
            response = BuildResponse(status='List success', code=200, message=f'Listing {repo_name}', data=data).build()
            response['page'] = page
            response['pageSize'] = pageSize
            response['total'] = len_fields
        except Exception as e:
            Model.rollback()
            print(e)
            data = {}
            response = BuildResponse(status='List failed', code=200, message=f'Listing failed {repo_name}', data=data).build()
            del response['data']
        return response

    @staticmethod
    def create(request):
        request_json = request.get_json(silent=True)
        request_json['is_delete'] = False

        try:
            row = Model(request_json)
            row.save()
            data = create_doc(row)
            response = BuildResponse(status='Create success', code=201, message=f'{repo_name} create success', data=data).build()
            return response
        except Exception as e:
            print(e)
            row.rollback()
            data = {}
            response = BuildResponse(status='Create failed', code=400, message=f'{repo_name} create failed', data=data).build()
            del response['data']
            return response

    @staticmethod
    def edit(id, request):
        request_json = request.get_json(silent=True)

        try:
            row = Model.query.get(id)

            if row is not None: #change this
                for key in request_json.keys():
                    setattr(row,key,request_json(key))
                row.updated_at = datetime.datetime.now()

                row.save()

                data = create_doc(row)

                response = BuildResponse(status='Edit success', code=201, message=f'{repo_name} edit success', data=data).build()
                return response
            else:
                data = {}
                response = BuildResponse(status='Edit failed', code=404, message=f'{repo_name} not found', data=data).build()
                del response['data']
                return response
        except:
            data = {}
            response = BuildResponse(status='Edit failed', code=404, message=f'{repo_name} edit failed', data=data).build()
            del response['data']
            return response
        
    @staticmethod
    def show(id):
        try:
            row = Model.query.get(id)
            if row is not None:
                data = create_doc(row)
                response = BuildResponse(status='Show success', code=200, message=f'Show {repo_name}', data=data).build()
                return response
            else:
                data = {}
                response = BuildResponse(status='Show failed', code=404, message=f'{repo_name} not found', data=data).build()
                del response['data']
                return response
        except:
            data = {}
            response = BuildResponse(status='Show failed', code=404, message=f'{repo_name} not found', data=data).build()
            del response['data']
            return response

    @staticmethod
    def remove(id):
        try:
            row = Model.query.get(id)

            if row is not None:
                row.is_delete = True
                row.updated_at = datetime.datetime.now()

                row.save()

                data = create_doc(row)

                response = BuildResponse(status='Delete success', code=201, message=f'{repo_name} delete success', data=data).build()
                return response
            else:
                data = {}
                response = BuildResponse(status='Edit failed', code=404, message=f'{repo_name} not found', data=data).build()
                del response['data']
                return response
        except:
            data = {}
            response = BuildResponse(status='Edit failed', code=404, message=f'{repo_name} delete failed', data=data).build()
            del response['data']
            return response
    