from sqlalchemy.orm import relationship

from . import db_sql as db
from .base_sql import BaseSQLModel as BaseModel
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from werkzeug.security import generate_password_hash
from utils import string_to_date, generate_uuid

class User(db.Model, BaseModel):

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    place_of_birth = db.Column(db.Text, nullable=True)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    phone = db.Column(db.String(32), nullable=True)
    home_address = db.Column(db.Text, nullable=True)
   
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_delete = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    created_by = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=True)

    user = relationship('User',remote_side=[created_by])

    def __init__(self, field_dict:dict):
        self.place_of_birth = field_dict.get("place_of_birth")
        self.date_of_birth = string_to_date(field_dict.get("date_of_birth"))
        self.phone = field_dict.get("phone")
        self.home_address = field_dict.get("home_address")

        self.email = field_dict.get("email")
        self.first_name = field_dict.get("first_name")
        self.last_name = field_dict.get("last_name")
        self.password = generate_password_hash(field_dict.get("password"), method='sha256')
        self.is_admin = field_dict.get("is_admin")

        self.is_active = field_dict.get("is_active")
        self.is_delete = field_dict.get("is_delete")
        self.created_by = field_dict.get("created_by")
