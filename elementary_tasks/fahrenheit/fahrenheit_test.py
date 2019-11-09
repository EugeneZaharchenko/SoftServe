import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fahrenheit.fahrenheit import fahr, celc


class TestFahrenheitConverter(unittest.TestCase):

    def test_fahr_function_positive(self):
        in_fahr = fahr(10)
        expected_in_fahr = 50
        self.assertEqual(in_fahr, expected_in_fahr)
        # with self.assertRaises(ValueError):
        #     Fibonacci(12, 1)

    def test_fahr_function_negative(self):
        in_fahr = fahr(1)
        expected_in_fahr = 50
        self.assertNotEqual(in_fahr, expected_in_fahr)

    def test_celc_function_positive(self):
        in_celc = celc(32)
        expected_in_celc = 0
        self.assertEqual(in_celc, expected_in_celc)

    def test_celc_function_negative(self):
        in_celc = celc(1)
        expected_in_celc = 50
        self.assertNotEqual(in_celc, expected_in_celc)


if __name__ == "__main__":
    unittest.main()
