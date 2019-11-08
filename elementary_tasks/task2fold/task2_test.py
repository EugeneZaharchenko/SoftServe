import unittest
import sys
import os
from task2fold.task2 import Envelope, main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestEnvelopeClass(unittest.TestCase):

    def setUp(self) -> None:
        self.env1 = Envelope(100, 200)
        self.env2 = Envelope(50, 70)
        self.env3 = Envelope(50, 150)

    def test_class_instance(self):
        self.assertIsInstance(self.env1, Envelope)
        self.assertIsInstance(self.env2, Envelope)

    def test_if_parameters_invalid(self):
        with self.assertRaises(ValueError):
            self.env1.valid(0, 20)
            self.env1.valid(20, 0)
            self.env1.valid("str", 20)
            self.env1.valid(10, "str")

    def test_if_instance_is_greater(self):
        self.assertGreater(self.env1, self.env2)

    def test_if_instance_is_less(self):
        self.assertLess(self.env2, self.env1)


if __name__ == "__main__":
    unittest.main()
