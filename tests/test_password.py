import unittest
from password_tools import (
    check_strength,
    generate_password
)
class TestPasswordFunctions(unittest.TestCase):
    def test_weak_password(self):
        result = check_strength("hello")
        self.assertEqual(result, "Weak")
    def test_strong_password(self):
        result = check_strength("Python@123")
        self.assertEqual(result, "Strong")
