from flask import Blueprint, jsonify
from flask_cors import CORS

from ..models import Category, db
from ..questions.utils import abort_error_if_any

category = Blueprint("category", __name__)

# enable CORS for category
CORS(category, resources={r"/categories/*": {"origins": "*"}})


# CORS Headers
@category.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
    return response


@category.route("/categories")
def get_categories():
    error = False
    try:
        formatted_categories = Category.get()
        # extract cat type of each category
        categories_types = Category.get_types(formatted_categories)
    except Exception as e:
        error = True
    finally:
        db.session.close()

    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
        'categories': categories_types
    })
