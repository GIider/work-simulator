# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_object('work_simulator.settings')
app.url_map.strict_slashes = False

db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)

from . import models
from . import controllers