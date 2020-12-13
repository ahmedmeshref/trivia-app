from flask import Flask

from .models import setup_db, db, Question, Category
from conf import config_by_name


def create_app(config_object='development'):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_object])

    with app.app_context():
        setup_db(app)
        # import blueprints
        from .categories import categries
        from .questions import questions
        from .errors import errors

        # register blueprints
        app.register_blueprint(categries.category)
        app.register_blueprint(questions.question)
        app.register_blueprint(errors.error)

        return app
