# -*- coding: utf-8 -*-
import os

from flask import make_response

from . import app


TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', 'main.html')
with open(TEMPLATE_PATH) as f:
    HTML_TEMPLATE = f.read()


@app.route('/')
def index():
    return make_response(HTML_TEMPLATE)