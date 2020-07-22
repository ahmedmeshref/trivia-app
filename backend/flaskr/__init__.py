import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .models import setup_db, db, Question, Category
from config import config_by_name

QUESTIONS_PER_PAGE = 10


def create_app(config_object='development'):
    # create and configure the app
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config_by_name[config_object])

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    with app.app_context():
        setup_db(app)
        # import blueprints
        from .categories import categries
        from .questions import questions

        # register blueprints
        app.register_blueprint(categries.category)
        app.register_blueprint(questions.question)

        return app

