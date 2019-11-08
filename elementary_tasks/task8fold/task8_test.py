import unittest
import sys
import os
from task8fold.task8 import Fibonacci, main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestFibonacciClass(unittest.TestCase):

    def setUp(self) -> None:
        self.fib1 = Fibonacci(0, 13)
        self.fib2 = Fibonacci(10, 310)
        self.fib3 = Fibonacci(0, -12)

    def test_class_are_instances(self):
        self.assertIsInstance(self.fib1, Fibonacci)
        self.assertIsInstance(self.fib2, Fibonacci)
        self.assertIsInstance(self.fib3, Fibonacci)

    def test_validate_func_error_case(self):
        with self.assertRaises(ValueError):
            Fibonacci(12, 1)

    def test_fib_list_func_positive(self):
        result = self.fib1.fib_list()
        expected = ['0', '1', '1', '2', '3', '5', '8', '13']
        self.assertTrue(result, expected)

    def test_fib_list_func_negative(self):
        result = self.fib3.fib_list()
        expected = ['0', '1', '-1', '2', '-3', '5', '-8', '13']
        self.assertTrue(result, expected)


if __name__ == "__main__":
    unittest.main()
