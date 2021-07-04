from . import db_nosql as db
import uuid

class TestNoSQLModel(db.Model):
    uid = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    message = db.columns.Text(required=False)