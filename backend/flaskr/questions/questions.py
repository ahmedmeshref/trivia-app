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
    """
    error = False
    try:
        formatted_questions, tot_questions = query_questions(request)
        formatted_categories = Category.get()
    except Exception as e:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        # raise internal server error if error is True
        abort(500)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'categories': formatted_categories,
        'current_category': None
    })


@question.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question(question_id):
    """
    delete_question deletes a question from db with the given id
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
    if error:
        abort(500)
    return jsonify({
        'success': True,
    })


@question.route("/questions", methods=["POST"])
def create_question():
    data = get_request_data_or_400(request)
    question_ins = Question()
    attrs = dir(question_ins)
    # set attrs values of new_question instance from given request data
    new_question = set_attributes_all_required(question_ins, attrs, data)

    error = False
    try:
        new_question.insert()
        formatted_questions, tot_questions = query_questions(request)
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    # if error creating the question, raise exception (Unprocessable Request)
    if error:
        abort(422)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'current_category': None
    })


@question.route("/questions/search", methods=["POST"])
def search_questions():
    """handles POST request for getting search results. Results are paginated in groups of 10 questions.
    Note: if searchTerm == "" or None, all questions are going to be returned.
    """
    data = get_request_data_or_400(request)
    search_term = data.get("searchTerm", '')

    error = False
    try:
        formatted_questions, tot_questions = query_questions(request, text=search_term)
    except Exception as e:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        # if eternal server error
        abort(500)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'current_category': None
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
    get_item_or_404(Category, category_id)

    error = False
    try:
        formatted_questions, tot_questions = query_questions(request, cat_id=category_id)
    except Exception as e:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        # raise internal server error if error is True
        abort(500)
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'current_category': category_id
    })


'''
@TODO: 
Create a POST endpoint to get questions to play the quiz. 
This endpoint should take category and previous question parameters 
and return a random questions within the given category, 
if provided, and that is not one of the previous questions. 

TEST: In the "Play" tab, after a user selects "All" or a category,
one question at a time is displayed, the user is allowed to answer
and shown whether they were correct or not. 
'''


@question.route("/quizzes", methods=["POST"])
def get_questions_for_quiz():
    """ handles post requests for getting questions to play the quiz. Request should contain quiz_category (int) and
     previous questions (list).
    @rtype: json Object
    @returns: random questions within the given category
    """
    data = get_request_data_or_400(request)
    previous_questions = data.get("previous_questions")
    current_category = data.get("quiz_category")
    if not (current_category and get_item_or_404(Category, current_category)):
        # if not current category on the request body or given category id doesn't map to an existing category,
        # raise Bad Request error (400).
        abort(400)

    error = False
    try:
        questions = db.session.query(Question).filter(Question.id.notin_(previous_questions),
                                                      Question.category == str(current_category)).all()
        random_question = random.choice(questions)
        formatted_question = random_question.format()
    except Exception as e:
        error = True
    finally:
        db.session.close()

    if error:
        abort(500)
    return jsonify({
        'success': True,
        'question': formatted_question
    })
