import unittest
import sys
import os
from task5fold.task5 import NumToWords
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestNumToWordsClass(unittest.TestCase):

    def setUp(self) -> None:
        self.num0 = NumToWords(0)
        self.num1 = NumToWords(12543)

    def test_instance(self):
        self.assertIsInstance(self.num0, NumToWords)
        self.assertIsInstance(self.num1, NumToWords)

    def test_class_instance_error(self):
        with self.assertRaises(ValueError):
            self.num3 = NumToWords("NoNum")

    def test_unit_convert_func(self):
        result0 = NumToWords.unit_convert(0)
        result1 = NumToWords.unit_convert(1)
        result19 = NumToWords.unit_convert(19)
        expected0 = "ноль"
        expected1 = "один"
        expected19 = "девятнадцать"
        self.assertEqual(result0, expected0)
        self.assertEqual(result1, expected1)
        self.assertEqual(result19, expected19)

    # def test_unit_two_convert_func(self):
    #     result15 = NumToWords.two_convert(15, 1)
    #     result30 = NumToWords.two_convert(330, 1)
    #     expected15 = "пятнадцать"
    #     expected30 = "тридцать"
    #     self.assertEqual(result15, expected15)
    #     self.assertEqual(result30, expected30)

    # def test_limit(self):
    #     self.assertIsInstance(self.num1.count_limit(), list)
    #     self.assertIsInstance(self.num15.count_limit(), list)
    #     self.assertEquals(self.num1.count_limit(), ['0'])
    #     self.assertEquals(self.num15.count_limit(), ['0', '1', '2', '3'])

    # def test_str(self):
    #     self.assertEquals(self.num1.__str__(), 'Sequence of numbers whose pow of 2 is less the 1 is: 0')
    #     self.assertEquals(self.num15.__str__(), 'Sequence of numbers whose pow of 2 is less the 15 is: 0, 1, 2, 3')


if __name__ == "__main__":
    unittest.main()
