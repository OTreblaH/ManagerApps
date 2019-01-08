from ManagerApp.app import db
import hashlib


class User(db.Model):
    __tableName__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    passwd = db.Column(db.String(150))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.criptopasswd()

    def criptopasswd(self):
        self.passwd = hashlib.sha224(self.passwd).hexdigest()




