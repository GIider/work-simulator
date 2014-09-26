# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_object('work_simulator.settings')

db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)

from . import decorator
from . import player
from . import exception
from . import models