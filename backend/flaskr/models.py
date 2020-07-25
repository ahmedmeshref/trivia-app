import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

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

    def __repr__(self):
        return f"<Question {self.question, self.category}>"

    def __dir__(self):
        return ["question", "answer", "category", "difficulty"]

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

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

    @staticmethod
    def get_types(formatted_categories):
        return [cat["type"] for cat in formatted_categories]

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }
