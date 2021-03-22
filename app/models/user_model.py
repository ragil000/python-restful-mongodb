import sys
from datetime import datetime
import pytz
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

timezone = pytz.timezone('Asia/Jakarta')
datetime = datetime.now(timezone)

class UserModel(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    role = db.StringField(required=True)
    created_at = db.DateTimeField(required=True, default=datetime)
    updated_at = db.DateTimeField(required=True, default=datetime)
    
    def __init__(self, *args, **kwargs):
        if 'password' in kwargs and '_created' not in kwargs:
            print('kok masuk sini')
            password = kwargs.get('password')
            if password:
                self.set_password(args, kwargs, password=password)
        super(UserModel, self).__init__(*args, **kwargs)

    def set_password(self, args, kwargs, password):
        kwargs['password'] = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    meta = {'collection': 'users'}