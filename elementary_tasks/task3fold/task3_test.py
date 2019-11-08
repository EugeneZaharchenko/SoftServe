import unittest
import sys
import os
from task3fold.task3 import Triangle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestTriangleClass(unittest.TestCase):

    def setUp(self) -> None:
        self.tr1 = Triangle("abc", 3, 4, 5)
        self.tr2 = Triangle("CBA", 30, 40, 50)

    def test_class_instance(self):
        self.assertIsInstance(self.tr1, Triangle)
        self.assertIsInstance(self.tr2, Triangle)
        with self.assertRaises(IndexError):
            self.tr3 = Triangle("NoTr", 1, 2, 3)

    def test_validate_func(self):
        result1 = self.tr1.valid("  abc ", 3, 4, 5)
        expected_result1 = "Abc", 3, 4, 5
        result2 = self.tr2.valid("  CBA ", 30, 40.0, 50.0)
        expected_result2 = "Cba", 30, 40, 50
        self.assertTrue(result1, expected_result1)
        self.assertTrue(result2, expected_result2)

    def test_area_func(self):
        result1 = self.tr1.area
        expected_result1 = 6.0
        result2 = self.tr2.area
        expected_result2 = 600.0
        self.assertTrue(result1, expected_result1)
        self.assertTrue(result2, expected_result2)

    def test_str_representation(self):
        expected_result1 = "Abc: 6 cm"
        expected_result2 = "Cba: 600 cm"
        self.assertEqual(self.tr1.__str__(), expected_result1)
        self.assertEqual(self.tr2.__str__(), expected_result2)


if __name__ == "__main__":
    unittest.main()
