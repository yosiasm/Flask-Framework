from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.base import object_mapper
db_sql = SQLAlchemy()


from .base_sql import BaseSQLModel
from .user import User as UserModel
# from .notifikasi import Notifikasi as NotifikasiModel
# from .role import Role as RoleModel

from flask.ext.cqlalchemy import CQLAlchemy
db_nosql = CQLAlchemy()

from .test_nosql import TestNoSQLModel
