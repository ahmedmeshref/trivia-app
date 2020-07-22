from flask import current_app, Blueprint, jsonify

from ..models import db, Category

category = Blueprint("category", __name__)


@category.route("/categories")
def get_categories():
    categories = db.session.query(Category).all()
    formatted_categories = [cat.format() for cat in categories]
    return jsonify({
        'success': True,
        'categories': formatted_categories
    })
