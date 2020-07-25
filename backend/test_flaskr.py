from os import path
import unittest
import json

from flaskr import create_app
from flaskr.models import setup_db, db, Question
from flaskr.questions.utils import QUESTIONS_PER_PAGE


class TriviaTestClass(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Initialize testing app"""
        self.app = create_app('testing')
        self.client = self.app.test_client()

        with self.app.app_context():
            # setUp db on the app
            setup_db(self.app)

        self.new_question = {
            "question": "Do you love Coding?",
            "answer": "yes",
            "category": 5,
            "difficulty": 3
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_questions(self):
        response = self.client.get("/questions?page=1")
        data = json.loads(response.data)

        if data:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(len(data["questions"]), QUESTIONS_PER_PAGE)
            self.assertTrue(len(data["categories"]))
            self.assertTrue(data["total_questions"])

    def test_delete_user_given_existing_id(self):
        # test deleting existing question with id = 2
        response = self.client.delete("/questions/2")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404_delete_user_with_non_existing_id(self):
        response = self.client.delete("/questions/1000")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Resource Not Found')

    def test_create_question(self):
        response = self.client.post("/questions", json=self.new_question)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), QUESTIONS_PER_PAGE)
        self.assertTrue(data["total_questions"])

    def test_400_create_question_with_data_missing(self):
        response = self.client.post("/questions")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Bad Request')

    def test_405_create_question_on_wrong_endpoint(self):
        response = self.client.post("/questions/1", json=self.new_question)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Method Not Allowed')

    def test_get_questions_by_category(self):
        # test getting all questions for category 1
        response = self.client.get("/categories/1/questions")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["total_questions"])
        self.assertTrue(data["current_category"])

    def test_404_get_questions_of_non_existing_category(self):
        # test getting all questions for category 1000
        response = self.client.get("/categories/1000/questions")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Resource Not Found')

    def test_search_question_with_searchTerm(self):
        # test search questions with What keyword
        searchTerm = 'What'
        response = self.client.post("/questions/search", json={'searchTerm': searchTerm})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["total_questions"])

    def test_search_question_with_empty_string_searchTerm(self):
        # test get all questions in case of empty string searchTerm
        searchTerm = ''
        response = self.client.post("/questions/search", json={'searchTerm': searchTerm})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["total_questions"])

    def test_400_create_question_without_specifying_searchTerm(self):
        # test deleting existing question with id = 2
        response = self.client.post("/questions/search")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Bad Request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
