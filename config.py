from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Config(object):
    # app.config['MONGODB_DB'] = 'project1'
    MONGODB_HOST = os.getenv('DB_URI')
    # app.config['MONGODB_PORT'] = 12345
    # app.config['MONGODB_USERNAME'] = 'webapp'
    # app.config['MONGODB_PASSWORD'] = 'pwd123'
    SERVER_NAME = '127.0.0.1:3000'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # SECRET_KEY = environ.get('API_FLASK_SECRET_KEY')
    # VAULT_ADDR = environ.get('VAULT_ADDR')
    # VAULT_TOKEN = environ.get('VAULT_TOKEN')

app_config_dict = {
    'Production': ProductionConfig,
    'Development': DevelopmentConfig
}