from flask import Blueprint, jsonify, request
from flask_cors import CORS

from ..models import db, Category, Question
from .utils import *

question = Blueprint("question", __name__)

# enable CORS for questions
CORS(question, resources={r"/questions/*": {"origins": "*"}})


# CORS Headers
@question.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response


@question.route("/questions")
def get_questions():
    """
    get_questions handles GET requests for questions, including pagination (every 10 questions).
    """
    formatted_questions, tot_questions = Question.get(request)
    formatted_categories = Category.get()
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions': tot_questions,
        'categories': formatted_categories,
        'current_category': None
    })


'''
@TODO: 
Create an endpoint to DELETE question using a question ID. 

TEST: When you click the trash icon next to a question, the question will be removed.
This removal will persist in the database and when you refresh the page. 
'''


@question.route("/questions/<int:id>", methods=["DELETE"])
def delete_question(id):
    target_question = get_item_or_404(Question, id)
    target_question.delete()
    formatted_questions, tot_questions = Question.get(request)

    return jsonify({
        'success': True,
        'id': id,
        'questions': formatted_questions,
        'total_questions': tot_questions
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

'''
@TODO: 
Create error handlers for all expected errors 
including 404 and 422. 
'''
