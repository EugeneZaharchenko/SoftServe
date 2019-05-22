import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from task1fold.task1 import Chess


class TestNumberClass(unittest.TestCase):

    def setUp(self) -> None:
        self.fib = Chess(5, 10)

    # def tearDown(self):
    #     print('Task 7 tested')

    # def test_if_string(self):
    #     self.assertIsInstance(str, print(self.fib))

    def test_if_str_is_empty(self):
        self.assertEqual("", Chess(0,0))

    def test_if_str_is_not_empty(self):
        self.assertEqual("", Chess(15, 45))


if __name__ == "__main__":
    unittest.main()
