import os


class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/managerapp.db' % APPLICATION_DIR
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


