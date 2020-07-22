import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

from .questions.utils import pagination

# create a db instance
db = SQLAlchemy()


# setup db for the flask app instance
def setup_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


# questions table
class Question(db.Model):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category = Column(String)
    difficulty = Column(Integer)

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get(request):
        questions = db.session.query(Question).order_by(Question.id).all()
        formatted_questions = pagination(request, questions)
        return [formatted_questions, len(questions)]

    def format(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
        }


# Category table
class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    @staticmethod
    def get():
        categories = db.session.query(Category).all()
        formatted_categories = [cat.format() for cat in categories]
        return formatted_categories

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }
