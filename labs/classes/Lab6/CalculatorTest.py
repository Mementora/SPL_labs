import unittest
from unittest.mock import patch
from Lab2 import Solutions

class CalculatorTester(unittest.TestCase):
    def setUp(self):
        self.calculator = Solutions.Calculator()

    # Unit test of adding two numbers
    def test_add(self):
        self.assertEqual(self.calculator.add(5,5), 10)

    # Unit test of subtracting two numbers
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 3), 7)

    # Unit test of subtracting two numbers
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(12.5, 3.7), 46.25)

    # Unit test of subtracting two numbers
    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

    #Unit test of finding square root negative number
    def test_square_root_negative(self):
        self.assertEqual(self.calculator.square_root(-25), "Cannot take the square root of a negative number")

    #Unit test of dividing remainder by zero
    def test_remainder_divide_by_zero(self):
        result = self.calculator.remainder(10, 0)
        self.assertEqual(result, "Can't find the remainder when dividing by zero")

    #Unit test of placing invalid operator
    def test_invalid_operator(self):
        result = self.calculator.start_calculation()
        self.assertEqual(result, "Invalid operator")

    #Unit test of mock empty input
    @patch("builtins.input", side_effect=['', '5'])
    def test_mock_empty_input(self, mock_input):
        result = self.calculator.set_user_input(None, None)
        self.assertEqual(result, "Error: Empty input")

    #Unit test of exception of division by zero
    def test_exception_by_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10,0)
