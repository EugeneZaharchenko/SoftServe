import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from task2fold.task2 import Envelope


class TestEnvelopeClass(unittest.TestCase):

    def setUp(self) -> None:
        self.num1 = Number(1)
        self.num15 = Number(15)
        # self.num5 = Number(0)

    def tearDown(self):
        print('Task 2 tested')

    def test_validate(self):
        self.assertRaises(ValueError, self.num1.validate)

    def test_range(self):
        self.assertIs(self.num1.count_limit(), int)
        self.assertEqual(self.num1.count_limit(), 1)
        self.assertIs(self.num15.count_limit(), int)
        self.assertEqual(self.num15.count_limit(), 15)

    def test_instance(self):
        self.assertIsInstance(self.num1, Number)
        self.assertIsInstance(self.num15, Number)

    def test_limit(self):
        self.assertIsInstance(self.num1.count_limit(), list)
        self.assertIsInstance(self.num15.count_limit(), list)
        self.assertEquals(self.num1.count_limit(), ['0'])
        self.assertEquals(self.num15.count_limit(), ['0', '1', '2', '3'])

    def test_str(self):
        self.assertEquals(self.num1.__str__(), 'Sequence of numbers whose pow of 2 is less the 1 is: 0')
        self.assertEquals(self.num15.__str__(), 'Sequence of numbers whose pow of 2 is less the 15 is: 0, 1, 2, 3')


if __name__ == "__main__":
    unittest.main()
