import unittest
from Lab2 import Solutions

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Solutions.Calculator()

    # Unit test of adding two numbers
    def test_add(self):
        self.assertEqual(self.calculator.add(5, 5), 10)

    # Unit test of subtracting two numbers
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 3), 7)

    # Unit test of subtracting two numbers
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(12.5, 3.7), 46.25)

    # Unit test of subtracting two numbers
    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

    # Unit test of dividing by zero
    def test_division_by_zero(self):
        self.assertEqual(self.calculator.divide(0, 5), "Can't divide by zero")

    # Unit test of empty input
    def test_empty_input(self):
        self.assertEqual(self.calculator.user_input(), None)