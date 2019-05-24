import unittest
import sys
import os
from task6fold.task6 import LuckyNumber
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestLuckyNumberClass(unittest.TestCase):

    def setUp(self) -> None:
        self.lucky_ticket = LuckyNumber("mode.txt")

    def test_class_instance(self):
        self.assertIsInstance(self.lucky_ticket, LuckyNumber)

    def test_class_instance_error(self):
        with self.assertRaises(IOError):
            self.not_lucky_ticket = LuckyNumber("No_file.txt")

    def test_validate_func(self):
        result = LuckyNumber.validate("654321")
        expected = 654321
        self.assertEqual(result, expected)
        with self.assertRaises(ValueError):
            self.not_valid_ticket = LuckyNumber.validate("123")

    def test_mode_and_read_func(self):
        result = self.lucky_ticket.mode_and_read()
        expected = "piter"
        self.assertEqual(result, expected)
        result1 = self.lucky_ticket.mode_and_read()
        expected1 = "moskow"
        self.assertNotEqual(result1, expected1)

    def test_happy_func_piter(self):
        result1 = self.lucky_ticket.happy("122100")
        result2 = self.lucky_ticket.happy("150303")
        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_happy_func_moskow(self):
        self.lucky_ticket1 = LuckyNumber("mode.txt")
        self.lucky_ticket1._mode = "moskow"
        result1 = self.lucky_ticket1.happy("122100")
        result2 = self.lucky_ticket1.happy("150303")
        self.assertFalse(result1)
        self.assertTrue(result2)

    def test_count_func(self):
        result = self.lucky_ticket.count()
        expected = 1
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
