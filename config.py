import os

# Database setting
POSTGRES_URL= os.environ.get('POSTGRES_URL', '10.10.10.101') #server
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432) #server
# POSTGRES_URL= os.environ.get('POSTGRES_URL', '') #local
# POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5437) #local
POSTGRES_USER = os.environ.get('POSTGRES_USER', '')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD','')
POSTGRES_DB = os.environ.get('POSTGRES_DB', '')

def get_env_variable(name) -> str:
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

class Config(object):
    DEBUG = True
    # SQLAlchemy
    uri_template = 'postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'
    SQLALCHEMY_DATABASE_URI = uri_template.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PASSWORD,
        url=POSTGRES_URL,
        port=POSTGRES_PORT,
        db=POSTGRES_DB)

    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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
