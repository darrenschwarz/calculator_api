import unittest
from app import app

class CalculatorAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add(self):
        response = self.app.get('/add?num1=1&num2=2')
        data = response.get_json()
        self.assertEqual(data['result'], 3.0)

if __name__ == '__main__':
        unittest.main()
