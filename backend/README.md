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

### Getting Started 

- Base URL: At the present, this API can only run locally and it is not hosted as a base URL. This backend is hosted 
at the default, `http://127.0.0.1:5000/`, which is set as a proxy in frontend configurations.

- Authentication: This version of the app doesn't require Authentication or API keys. 


### Errors Handling 

Rest plants returns errors as JSON objects in the following format:
```   
{
    'success': False,
    'error': 404,
    'message': 'Resource Not Found'
}
```

#### Overview:

In general, the error codes that indicate failure of the API request are: 
- Codes in range `4xx` indicate the failure of the request. These errors can be programmatically corrected. You can get
more information about these errors, from the API response body attributes such as message, to fix them.
- Codes in range `5xx` indicate the failure of the request due to internal server errors. Running your API request again
might solve these error.


#### Types of Errors:

| Error Code            | Code
| -------------         | ------------
| Bad Request           | 400 
| Resource Not Found    | 404 
| Method Not Allowed    | 405 
| Not Processable       | 422 
| Internal Server Error | 500 



### API Endpoints

Below are described the REST endpoints available.

#### Get All Questions 

- Sample Request:
    
    `curl -X GET http://127.0.0.1:5000/questions`

- Attributes:

    - `Optional` Page: you can specific the desired results page in the request body as follows:
    
        `curl -X GET http://127.0.0.1:5000/questions?page={number}`
        
        `curl -X GET http://127.0.0.1:5000/questions?page=2`

- Response: 

    - Returns json object with a list of 10 question objects, total_questions, success value, and list of categories. 
    - Results are paginated in groups of 10. 
    
    ```
    {
      "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
      ],
      "current_category": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
      ],
      "questions": [
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3,
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1,
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?"
        },
        {
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3,
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4,
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2,
          "id": 12,
          "question": "Who invented Peanut Butter?"
        },
        {
          "answer": "Lake Victoria",
          "category": 3,
          "difficulty": 2,
          "id": 13,
          "question": "What is the largest lake in Africa?"
        },
        {
          "answer": "The Palace of Versailles",
          "category": 3,
          "difficulty": 3,
          "id": 14,
          "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
          "answer": "Agra",
          "category": 3,
          "difficulty": 2,
          "id": 15,
          "question": "The Taj Mahal is located in which Indian city?"
        },
        {
          "answer": "Escher",
          "category": 2,
          "difficulty": 1,
          "id": 16,
          "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        }
      ],
      "success": true,
      "total_questions": 21
    }
    ```
    
#### Get All Categories 

- Sample Request:
    
    `curl -X GET http://127.0.0.1:5000/categories`

- Response: 

    - Returns json object with a list of categories, and success value. 
    ```
    {
      "categories": [
        "Science", 
        "Art", 
        "Geography", 
        "History", 
        "Entertainment", 
        "Sports"
      ], 
      "success": true
    }
    ```
    
####  Create New Question
    
- Sample Request:
    
    `curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question": "Do you love Coding?", "answer": "yes", "category": 1, "difficulty": 3}'`
    
    > Note: all the fields required (question, answer, category, difficulty) should specified on the request body.
    
- Response: 
    - Returns json object with a list of question objects, success value, new_plant_id, total_questions, and current_category value.
    ```
    {
      "current_category": null,
      "questions": [
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3,
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1,
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?"
        },
        {
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3,
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4,
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2,
          "id": 12,
          "question": "Who invented Peanut Butter?"
        },
        {
          "answer": "Lake Victoria",
          "category": 3,
          "difficulty": 2,
          "id": 13,
          "question": "What is the largest lake in Africa?"
        },
        {
          "answer": "The Palace of Versailles",
          "category": 3,
          "difficulty": 3,
          "id": 14,
          "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
          "answer": "Agra",
          "category": 3,
          "difficulty": 2,
          "id": 15,
          "question": "The Taj Mahal is located in which Indian city?"
        },
        {
          "answer": "Escher",
          "category": 2,
          "difficulty": 1,
          "id": 16,
          "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        }
      ],
      "success": true,
      "total_questions": 22
    }
    ```
    
####  Delete Existing Plant
    
- Sample Request:

    `curl -X DELETE http://127.0.0.1:5000/questions/{id}`   
   
    `curl -X DELETE http://127.0.0.1:5000/questions/9` 
    
    > Note: if the provided id doesn't match with any existing question id, a 404 error will be returned.

- Response: 
    - Returns json object with a success value.
    ```
    {
      "success": true
    }
    ```








## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


##  Author

- [Ahmed Meshref]("https://github.com/ahmedmeshref")
