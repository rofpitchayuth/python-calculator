import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    # Subtract test cases
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    # Multiply test cases
    def test_multiply_simple(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    # Divide test cases
    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide_inexact(self):
        self.assertEqual(self.calc.divide(9, 2), 4)  # Integer division

    # Modulo test cases
    def test_modulo_simple(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)
if __name__ == '__main__':
    unittest.main()