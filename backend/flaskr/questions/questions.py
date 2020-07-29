import random

from flask import Blueprint, jsonify, request
from flask_cors import CORS

from ..models import db, Category, Question
from .utils import *

question = Blueprint("question", __name__)

# enable CORS for questions
cors = CORS(question, resources={r"/question/*": {"origins": "*"}})


# CORS Headers
@question.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
    return response


@question.route("/questions", methods=["GET"])
def get_questions():
    """handles GET requests for getting questions questions. Results are paginated in groups of 10 questions.
    @rtype: JSON object
    """
    error = False
    try:
        formatted_questions, tot_questions = query_questions(request)
        formatted_categories = Category.get()
        # extract cat type of each category
        categories_types = Category.get_types(formatted_categories)
    except Exception as e:
        error = True
    finally:
        db.session.close()

    # raise internal server error if error is True
    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'categories': categories_types,
        'current_category': categories_types
    })


@question.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question(question_id):
    """handles delete questions from db with the given id.
    """
    target_question = get_item_or_404(Question, question_id)
    error = False
    try:
        target_question.delete()
    except Exception as e:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
    })


@question.route("/questions", methods=["POST"])
def create_question():
    """ handles creating new question with a post request.
    @rtype: JSON object
    """
    data = get_request_data_or_400(request)
    question_ins = Question()
    attrs = dir(question_ins)
    # set attrs values of new_question instance from given request data
    new_question = set_attributes_all_required(question_ins, attrs, data)

    error = False
    try:
        new_question.insert()
        formatted_questions, tot_questions = query_questions(request)
    except Exception as e:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    # raise exception (Unprocessable Request), if error is True
    abort_error_if_any(error, 422)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'current_category': None
    })


@question.route("/questions/search", methods=["POST"])
def search_questions():
    """handles POST request for getting search results with a given searchTerm. Results are paginated in groups of 10
    questions. Note: if searchTerm == "" or None, all questions in db are returned.
    """
    data = get_request_data_or_400(request)
    search_term = data.get("search_term", '')

    error = False
    try:
        formatted_questions, tot_questions = query_questions(request, text=search_term)
        categories = Category.get()
    except Exception as e:
        error = True
    finally:
        db.session.close()

    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'current_category': categories
    })


@question.route("/categories/<int:category_id>/questions", methods=["GET"])
def get_questions_by_cat(category_id):
    """handles get questions based on category id. Results are paginated in groups of 10 questions.
    @type category_id: int
    @param category_id
    @rtype: json Object
    @returns: json object with results value, list of questions, number of total questions, current category id.
    """
    # verify a given category_id maps to an existing category. If not, raise 404 (Not Found) error.
    category = get_item_or_404(Category, category_id)

    error = False
    try:
        formatted_questions, tot_questions = query_questions(request, cat_id=category_id)
        all_categories = Category.get()
    except Exception as e:
        error = True
    finally:
        db.session.close()

    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'current_category': category.format(),
        'categories': all_categories
    })


@question.route("/quizzes", methods=["POST"])
def get_questions_for_quiz():
    """ handles post requests for getting questions to play the quiz. Request should contain quiz_category (int) and
     previous questions (list).
    @rtype: json Object
    @returns: random questions within the given category
    """
    data = get_request_data_or_400(request)

    # Get parameters from JSON Body.
    previous_questions = data.get("previous_questions", [])
    current_category = data.get("quiz_category", None)
    if current_category:
        if current_category['id'] == 0:
            current_category = None
        else:
            # verify that a given category maps to an existing object in db.
            get_item_or_404(Category, current_category['id'])

    error = False
    try:
        if not current_category:
            # if no category was giving or ALL is chosen
            questions = db.session.query(Question).filter(Question.id.notin_(previous_questions)).all()
        else:
            questions = db.session.query(Question).filter(Question.id.notin_(previous_questions),
                                                          Question.category == current_category["id"]).all()

        formatted_question = None
        if questions:
            random_question = random.choice(questions)
            formatted_question = random_question.format()
    except Exception as e:
        error = True
    finally:
        db.session.close()

    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
        'question': formatted_question
    })
