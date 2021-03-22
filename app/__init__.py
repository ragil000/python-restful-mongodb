from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

from flask import Blueprint
from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

db = MongoEngine()

from config import app_config_dict
from app.routes import blueprints

def register_blueprints(app):
    for key in blueprints:
        app.register_blueprint(blueprints[key])
        print('===> blueprint for {} registered!'.format(key))

def configure_database(app):
    @app.before_first_request
    def create_default():
        # db.drop_all()
        # db.connect
        print('jalan lagi')

def create_app(path):
    app = Flask(__name__, static_folder='publics')
    app.config.from_object(app_config_dict['Development'])
    app.production = not app.config['DEBUG']
    app.path = path
    CORS(app) # CORS handler
    register_blueprints(app)
    configure_database(app)
    print('aku di print lagi')
    # if app.production:
    #     app.vault_client = create_vault_client(app)
    return app