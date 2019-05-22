import unittest
import sys
import os
from task4fold.task4 import FindReplace
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestFindReplaceClass(unittest.TestCase):

    def setUp(self) -> None:
        self.find_replace1 = FindReplace("words_test.txt", "Lorem")
        self.find_replace2 = FindReplace("words_test.txt", "Lorem")

    def test_class_instance(self):
        self.assertIsInstance(self.find_replace3, FindReplace)
        with self.assertRaises(IOError):
            self.find_replace3 = FindReplace("words.txt", "Lorem")

    def test_count_func(self):
        result1 = self.find_replace1.count("Lorem")
        result2 = self.find_replace2.count("Budda")
        expected1 = 5
        expected2 = 0
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)

    # def test_count_func(self, find):
    #     result1 = self.tr1.area
    #     expected_result1 = 6.0
    #     result2 = self.tr2.area
    #     expected_result2 = 600.0
    #     self.assertTrue(result1, expected_result1)
    #     self.assertTrue(result2, expected_result2)

    def test_str_representation(self):
        expected1 = "String lorem in given file was found 0 times."
        # expected_result2 = "String {str_find} in given file was found {count} times. " \
        #                    "Requested string was replaced for {rep}."
        self.assertEqual(self.find_replace1.__str__(), expected1)
        # self.assertEqual(self.find_replace2.__str__(), expected_result2)


if __name__ == "__main__":
    unittest.main()
