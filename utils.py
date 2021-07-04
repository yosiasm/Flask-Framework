import os
import jwt
from datetime import datetime, timedelta
from flask import Request
from werkzeug.utils import secure_filename
from config import Config
import uuid


# App Secret Key
SECRET_KEY = "986f18c894c73ed51aee9ee1c2a3eca620a5a75ae80670e8"

# App Sesion expaired with hour
SESSION_EXPIRATION = 4

class BuildResponse():
    def __init__(self, status, code, message, data, **kwargs):
        
        if status is not None:
            self.status = status
        
        if code is not None:
            self.code = code
        
        if message is not None:
            self.message = message

        if data is not None:
            self.data = data

    def build(self):
        reponse = {
            "status": self.status,
            "code": self.code,
            "message" : self.message,
            "data": self.data
        }
        return reponse

def generate_token(data):
    _expired = datetime.now() + timedelta(hours=SESSION_EXPIRATION)

    token = jwt.encode(data, SECRET_KEY, algorithm="HS256")

    response = {
        "token": token,
        "expired": _expired.strftime("%Y-%m-%d %H:%M:%S")
    }

    return response

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token.replace('Bearer ',''), SECRET_KEY,algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def list_default_param(request:Request):
    page = int(request.args.get('page', 1))
    pageSize = int(request.args.get('pageSize', 10))
    is_delete = request.args.get('is_delete', False)
    return page, pageSize, is_delete

def string_to_date(string_date:str):
    return datetime.strptime(string_date, format="%Y-%m-%d")

def save_file(file, path:str, subfile:str="", prefix:str="", infix:str="", postfix:str=""):
    '''
        file = request.files['file']
    '''
    filename = secure_filename(file.filename)
    store_path = path
    print(store_path)
    split_tup = os.path.splitext(filename)
    file_extension = split_tup[1]
    filename = split_tup[0]
    if file_extension not in Config.FILE_EXTENSION:
        return False, f"Extensi File Salah ({file.filename})"
    if not prefix:
        prefix = str(int(datetime.now().timestamp()))
    filename = '_'.join([x for x in [prefix, infix, filename, postfix] if x])
    filename = filename.replace("/", "-")
    subfile = subfile+'/' if subfile else ""
    filename = f'{subfile}{filename}{file_extension}'
    try:
        print(filename)
        file.save(os.path.join(store_path, filename))
        return True, filename
    except Exception as e:
        print(e)
        return False, f"Gagal Menyimpan {file.filename}"

def generate_uuid():
    return str(uuid.uuid4())