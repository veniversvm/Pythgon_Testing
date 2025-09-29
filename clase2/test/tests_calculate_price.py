import unittest
from src.calculator import sum, subtrac, multiply, divide

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5
        assert sum(2, 3.0) == 5.0
        assert sum(2, -3) == -1

    # para que funcionen los metodos debe empezaar por 'test_nombre_metodo"
    def test_subtrac(self):
        assert subtrac(5, 3) == 2
        assert subtrac(3, 5) == -2

    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(-2.0 , -2) == 4.0
        assert multiply(2, 0) == 0

    def test_divide(self):
        assert divide(9, 3) == 3
        with self.assertRaises(ValueError):
            divide(10, 0)
