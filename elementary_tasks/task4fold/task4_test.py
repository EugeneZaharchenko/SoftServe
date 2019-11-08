import unittest
import sys
import os
from task4fold.task4 import FindReplace
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestFindReplaceClass(unittest.TestCase):

    def setUp(self) -> None:
        self.find_replace1 = FindReplace("words_test.txt", "Lorem")
        self.find_replace2 = FindReplace("words_test.txt", "Budda")

    def test_class_instance(self):
        self.assertIsInstance(self.find_replace1, FindReplace)

    def test_class_instance_error(self):
        with self.assertRaises(IOError):
            self.find_replace3 = FindReplace("words.txt", "Lorem")

    def test_count_func(self):
        result1 = self.find_replace1.count("Lorem")
        result2 = self.find_replace2.count("Budda")
        expected1 = 5
        expected2 = 0
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)

    def test_str_representation(self):
        result1 = self.find_replace1.__str__()
        expected1 = "String lorem in given file was found 5 times."
        result2 = self.find_replace2.__str__()
        expected2 = "String budda in given file was found 0 times."
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)


if __name__ == "__main__":
    unittest.main()
