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
    def test_password_length(self):
        password = generate_password(12)
        self.assertEqual(len(password), 12)
    def test_short_password(self):
         with self.assertRaises(ValueError):
            generate_password(5)
if __name__ == "__main__":
    unittest.main()
