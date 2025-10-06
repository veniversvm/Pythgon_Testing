import unittest
from src.calculator import sum, subtrac, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(4, sum(2,2))

    def test_subtraction(self):
        self.assertEqual(3, subtrac(5, 2))

    def test_multipli(self):
        self.assertEqual(35, multiply(7,5))

    def test_divide(self):
        self.assertEqual(3, divide(9,3))

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(0,0)
    pass