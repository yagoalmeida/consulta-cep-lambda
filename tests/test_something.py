import unittest
from src.lambda_function import handler


class TestSomething(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_something(self):
        response = handler({}, {})
        self.assertEqual(response.get("statusCode"), 200)
