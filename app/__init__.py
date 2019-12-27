import os
from flask import request, jsonify, abort, make_response
from flask_api import FlaskAPI
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup

# local import
from instance.config import app_config
from app.analyzer import analyze_case

ALLOWED_EXTENSIONS = {'html'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route('/api/v1/processos/', methods=['POST',])
    def processos():
        if 'file' not in request.files:
            return make_response(jsonify({"response": "Nenhum arquivo foi encontrado!"}), 404)

        file = request.files['file']

        if file.filename == '':
            return make_response(jsonify({"response": "Arquivo sem nome"}), 400)
        
        if file and allowed_file(file.filename):
            file = file.read()
            soup = BeautifulSoup(file, 'html.parser')
            response = analyze_case(soup)
            return make_response(jsonify(response), 201)
        
    return app
