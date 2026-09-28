import unittest
from validators import (
    validate_username,
    validate_password,
    validate_length
)
class TestValidators(unittest.TestCase):
    def test_valid_username(self):
        result, message = validate_username("student123")
        self.assertTrue(result)
    def test_empty_username(self):
        result, message = validate_username("")
        self.assertFalse(result)
     def test_valid_password(self):
        result, message = validate_password("Python@123")
        self.assertTrue(result)
    def test_short_password(self):
        result, message = validate_password("abc")
        self.assertFalse(result)
    def test_valid_length(self):
        result, value = validate_length("12")
        self.assertTrue(result)
        self.assertEqual(value, 12)
    def test_invalid_length(self):
        result, value = validate_length("hello")
        self.assertFalse(result)
