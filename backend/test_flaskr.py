from os import path
import unittest
import json

from flaskr import create_app
from flaskr.models import setup_db, db, Question


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

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["questions"]))
        self.assertTrue(len(data["categories"]))
        self.assertTrue(data["total_questions"])

    def test_get_questions_with_no_results(self):
        response = self.client.get("/questions?page=1000")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
