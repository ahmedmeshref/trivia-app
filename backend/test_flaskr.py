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

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_questions_with_results(self):
        response = self.client.get("/questions?page=1")
        data = json.loads(response.data)

        if data:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(len(data["questions"]), QUESTIONS_PER_PAGE)
            self.assertTrue(len(data["categories"]))
            self.assertTrue(data["total_questions"])

    def test_404_get_questions_with_no_results(self):
        response = self.client.get("/questions?page=1000")
        data = json.loads(response.data)

        # no questions were found for a giveing page
        if not data:
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data["success"], False)
            self.assertEqual(data["message"], 'Resource Not Found')

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


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
