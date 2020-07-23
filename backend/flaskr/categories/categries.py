from flask import Blueprint, jsonify
from flask_cors import CORS

from ..models import Category

category = Blueprint("category", __name__)

# enable CORS for category
CORS(category, resources={r"/categories/*": {"origins": "*"}})


# CORS Headers
@category.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response


@category.route("/categories")
def get_categories():
    formatted_categories = Category.get()
    return jsonify({
        'success': True,
        'categories': formatted_categories
    })
