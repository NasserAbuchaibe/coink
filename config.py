import os

SECRET_KEY = 'test'
PWD = os.path.abspath(os.curdir)

DEBUG = True

# sqlite database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/coindb.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False
