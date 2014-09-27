# -*- coding: utf-8 -*-
import os

from flask import make_response, send_from_directory

from . import app, api_manager

TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', 'main.html')

# Not sure if this is necessary :s
for model_name in app.config['API_MODELS']:
    model_class = app.config['API_MODELS'][model_name]
    api_manager.create_api(model_class, methods=['GET', 'POST'])


def read_template():
    """Read the template file"""
    with open(TEMPLATE_PATH) as f:
        template = f.read()

    return template


@app.route('/')
def index():
    # We don't cache this so we can work with a live version
    # instead of having to restart the server each time
    return make_response(read_template())


@app.route('/js/<filename>')
def serve_javascript(filename):
    """Serve static javascript files"""
    directory = os.path.join(app.static_folder, 'js')

    return send_from_directory(directory=directory, filename=filename)