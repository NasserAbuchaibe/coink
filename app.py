from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uuid import FlaskUUID

import config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)
FlaskUUID(app)

db = SQLAlchemy(app)

from routes import *
