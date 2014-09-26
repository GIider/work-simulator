# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('work_simulator.settings')

db = SQLAlchemy(app)

from . import decorator
from . import player
from . import exception
