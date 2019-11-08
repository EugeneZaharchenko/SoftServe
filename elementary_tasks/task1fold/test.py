import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from task1fold.task1 import Chess


def multiply(x, y):
    return x * y


class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "Should be 50")


if __name__ == "__main__":
    unittest.main()