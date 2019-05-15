import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from task8fold.task8 import Fibonacci


class TestFibonacciClass(unittest.TestCase):

    def setUp(self) -> None:
        self.num1 = Fibonacci(0, 1)
        self.num1_5 = Fibonacci(1, 5)
        self.num5_9 = Fibonacci(5, 9)

    def tearDown(self):
        print('Task 8 tested')

    @unittest.expectedFailure
    def test_validate(self):
        self.assertIs(self.num1.start, self.num1.stop, int)
        self.assertIs(self.num1_5.start, self.num1_5.stop, int)
        self.assertIs(self.num5_9.start, self.num5_9.stop, int)

    def test_instance(self):
        self.assertIsInstance(self.num1, Fibonacci)
        self.assertIsInstance(self.num1_5, Fibonacci)
        self.assertIsInstance(self.num5_9, Fibonacci)

    def test_exact_val(self):
        self.assertEqual(self.num1.fib(0), 0)
        self.assertEqual(self.num1.fib(1), 1)
        self.assertEqual(self.num1_5.fib(5), 5)
        self.assertEqual(self.num5_9.fib(9), 34)

    def test_seq(self):
        self.assertEqual(self.num1.sequence(), None)

    def test_str(self):
        self.assertEqual(self.num1.__str__(), 'Fibonacci sequence for a given range 0-1 is: 0, 1')
        self.assertEqual(self.num1_5.__str__(), 'Fibonacci sequence for a given range 1-5 is: 1, 1, 2, 3, 5')
        self.assertEqual(self.num5_9.__str__(), 'Fibonacci sequence for a given range 5-9 is: 5, 8, 13, 21, 34')


if __name__ == "__main__":
    unittest.main()