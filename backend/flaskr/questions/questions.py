from flask import Blueprint, jsonify, request, abort
from flask_cors import CORS

from ..models import db, Category, Question
from .utils import *

question = Blueprint("question", __name__)

# enable CORS for questions
CORS(question, resources={r"/api/*": {"origins": "*"}})


# CORS Headers
@question.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response


@question.route("/questions", methods=["GET"])
def get_questions():
    """
    get_questions handles GET requests for questions, including pagination (every 10 questions).
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
        # if eternal server error
        abort(500)
    elif not formatted_questions:
        # no questions found
        abort(404)
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


'''
@TODO: 
Create an endpoint to POST a new question, 
which will require the question and answer text, 
category, and difficulty score.

TEST: When you submit a question on the "Add" tab, 
the form will clear and the question will appear at the end of the last page
of the questions list in the "List" tab.  
'''


@question.route("/questions", methods=["POST"])
def create_question():
    res = request.get_json()
    question_ins = Question()
    attrs = dir(question_ins)
    # set attrs values of new_question instance from given request data
    new_question = set_attributes_all_required(question_ins, attrs, res)

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



'''
@TODO: 
Create a POST endpoint to get questions based on a search term. 
It should return any questions for whom the search term 
is a substring of the question. 

TEST: Search by any phrase. The questions list will update to include 
only question that include that string within their question. 
Try using the word "title" to start. 
'''

'''
@TODO: 
Create a GET endpoint to get questions based on category. 

TEST: In the "List" tab / main screen, clicking on one of the 
categories in the left column will cause only questions of that 
category to be shown. 
'''

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
