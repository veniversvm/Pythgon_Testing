import unittest
from src.calculator import sum, subtrac

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5
        assert sum(2, 3.0) == 5.0
        assert sum(2, -3) == -1

    # para que funcionen los metodos debe empezaar por 'test_nombre_metodo"
    def test_subtrac(self):
        assert subtrac(5, 3) == 2
        assert subtrac(3, 5) == -2
