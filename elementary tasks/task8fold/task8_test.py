import unittest
import sys
import os
from task8fold.task8 import Fibonacci
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestFibonacciClass(unittest.TestCase):

    def setUp(self) -> None:
        self.fib1 = Fibonacci(0, 123)
        self.fib2 = Fibonacci(10, 310)

    def test_class_instance(self):
        self.assertIsInstance(self.fib1, Fibonacci)
        self.assertIsInstance(self.fib2, Fibonacci)

    def test_validate_func_negative(self):
        with self.assertRaises(ValueError):
            Number.validate("NoNum")

    def test_range_check_func_positive(self):
        result = Number.range_check(100)
        expected = 100
        self.assertTrue(result, expected)

    def test_range_check_func_negative(self):
        with self.assertRaises(IndexError):
            Number.range_check(-10)

    def test_count_limit_func(self):
        result1 = self.num1.count_limit()
        expected1 = ['1', '2', '3']
        self.assertEqual(result1, expected1)

    def test_str_representation(self):
        expected = "Sequence of numbers whose pow of 2 is less the 10 is: 1, 2, 3"
        result = self.num1.__str__()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
