import os

SECRET_KEY = 'test'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/coindb.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False