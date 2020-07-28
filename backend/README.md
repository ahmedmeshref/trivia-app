# Full Stack Trivia API Backend
**Version 1.0.0**

A RESTful API that serves data to the trivia game. Using the Trivia API enables the user to add, delete, update, set questions, and play the game choosing a specific category.

> Note: All of the backend code follows the [PEP8 guidelines]("https://www.python.org/dev/peps/pep-0008/").

## Getting Started

### Technology Used

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we are use handle the lightweight sqlite database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension used to handle cross origin requests from our frontend server. 


### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Edit Configurations
Navigate to `/backend/config.py` and change the following:
```
SECRET_KEY = "Enter random key for the app's Config, DevelopmentConfig, TestingConfig classes"
SQLALCHEMY_DATABASE_URI = "dialect+driver://username:password@host:port/database". For more information about setting the URI, visit Flask Configuration.
```

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python wsgi.py  
# OR 
python3 wsgi.py
```
From your browser, navigate to `http://127.0.0.1:5000/`.



### Testing
To run the tests, from within the `backend` directory, excute:
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


## API Reference

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


##  Author

- [Ahmed Meshref]("https://github.com/ahmedmeshref")
