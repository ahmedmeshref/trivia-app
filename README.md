# Full Stack API Final Project

## Introduction

Trivia is a full-stack web application built to enrich and enhance the information of the users in different fields, categories, through general questions in the related area of interest. Trivia has the following features:

1) Display questions - both all questions and by field (category). Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

## Motivation

With people being busy visiting e-commerce and accessories application, The idea of trivia was born to be a light and interesting game to attract people to spend their free time enhancing their general knowledge. The trivia game is offering this via an interesting game that lets the user choose their field of interest and ask them related questions with points to earn if they have the correct answer. 

## Main Files: Project Structure
```
├── README.md
├── backend *** Contains API and test suit. 
|    ├── __init__.py
│    ├── README.md *** Contains backend server setup and API documentation
│    ├── config.py *** Contains app configuration for test and development environments.
│    ├── test_flaskr.py *** Contains unittest for testing the functionality.
│    ├── trivia.psql *** database dumb, restore with "psql trivia < trivia.psql"
│    ├── wsgi.py *** contains run app information, used to run the API. 
│    ├── flaskr  
|    |    ├── __init__.py *** App creation & API endpoints.
|    |    ├── models.py *** contains database tables implementation and db setup.
|    |    ├── categories *** categories blueprint file.
│    |          └── categories.py *** contains all functionality for the categories blueprint.
|    |    ├── errors *** errors blueprint file.
│    |          └── errors.py *** contains all errors' functions.
|    |    └── questions *** questions blueprint file.
|    |          ├── utils.py *** contains utils functionality used accros all blueprints.
|    |          └── questions.py *** contains all questions' blueprint functions.
│    └── requirements.txt *** The dependencies to be installed with "pip3 install -r requirements.txt"
|
└── frontend *** start frontend with "npm start"
    ├── README.md *** Contains Frontend Setup 
    └── src
        └── components *** Contains React Components
```

## Setup Project locally

Clone project repository by running `git clone "https://github.com/ahmedmeshref/trivia-app.git"`. To understand how to setup the backend API and front end, look at the documentation in each file.

### Backend

The `./backend` directory contains a completed Flask and SQLAlchemy server. head to [`./backend/`](./backend/README.md) for more information about the setup and app running.


### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. head to [`./frontend/`](./frontend/README.md) for more information about the setup and app running.


## Contributions:

All contributions are welcomed. Please work on your own branch and create a merge request to be reviewed and accepted.

## Authors

- Ahmed Meshref
