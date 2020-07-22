from flask import Blueprint, jsonify

from ..models import Category

category = Blueprint("category", __name__)


@category.route("/categories")
def get_categories():
    formatted_categories = Category.get_categories()
    return jsonify({
        'success': True,
        'categories': formatted_categories
    })
