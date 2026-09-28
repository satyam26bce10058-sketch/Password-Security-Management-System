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
