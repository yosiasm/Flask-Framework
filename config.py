import os
from cassandra.auth import PlainTextAuthProvider

# SQL Database setting
MARIADB_URL= os.environ.get('MARIADB_URL', 'localhost') #local
MARIADB_PORT = os.environ.get('MARIADB_PORT', 3306) #local
MARIADB_USER = os.environ.get('MARIADB_USER', 'root')
MARIADB_PASSWORD = os.environ.get('MARIADB_PASSWORD','12qwaszx')
MARIADB_DB = os.environ.get('MARIADB_DB', 'test_db')

# NoSQL Database setting
CASSANDRA_HOST = ['127.0.0.1']
CASSANDRA_KEYSPACE = 'test-db'
CASSANDRA_USER = 'cassandra'
CASSANDRA_PASSWORD = 'cassandra'

def get_env_variable(name) -> str:
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

class Config(object):
    DEBUG = True
    # SQLAlchemy
    uri_template = 'mysql+pymysql://{user}:{pw}@{url}:{port}/{db}'
    SQLALCHEMY_DATABASE_URI = uri_template.format(
        user=MARIADB_USER,
        pw=MARIADB_PASSWORD,
        url=MARIADB_URL,
        port=MARIADB_PORT,
        db=MARIADB_DB)

    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CQLAlchemy
    CASSANDRA_HOST=CASSANDRA_HOST
    CASSANDRA_KEYSPACE=CASSANDRA_KEYSPACE
    auth_provider = PlainTextAuthProvider(username=CASSANDRA_USER, password=CASSANDRA_PASSWORD)
    CASSANDRA_SETUP_KWARGS = {
        'auth_provider': auth_provider
    }


    # API settings
    # API_PAGINATION_PER_PAGE = 10
    FILE_EXTENSION = ['.pdf','.docx','.doc','.jpg']


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    MAX_CONTENT_PATH = 2 * 1024 * 1024
    DEBUG = False


def get_config(env=None):
    if env is None:
        try:
            env = get_env_variable('ENV')
        except Exception:
            env = 'development'
            print('env is not set, using env:', env)

    if env == 'production':
        return ProductionConfig()

    return DevelopmentConfig()
