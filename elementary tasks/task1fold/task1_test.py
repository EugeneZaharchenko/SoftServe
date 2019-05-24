import unittest
import sys
import os
from task1fold.task1 import Chess
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestChessClass(unittest.TestCase):

    def setUp(self) -> None:
        self.chess = Chess(2, 10)

    def test_valid_func(self):
        with self.assertRaises(ValueError):
            Chess.valid("NoNum", "n")

    def test_class_instance(self):
        self.assertIsInstance(self.chess, Chess)

    def test_if_str_is_not_empty(self):
        result = self.chess.__str__()
        expected = "* * * * * * * * * * \n * * * * * * * * * * "
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
