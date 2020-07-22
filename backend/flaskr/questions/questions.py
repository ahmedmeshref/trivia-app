from flask import current_app, Blueprint

question = Blueprint("question", __name__)


@question.route("/")
def home():
    return "I am bp from question"
