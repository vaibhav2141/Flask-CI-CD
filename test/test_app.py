import unittest
from app import app

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from Flask App", response.data)

    def test_health(self):
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"UP", response.data)

if __name__ == "__main__":
    unittest.main()
