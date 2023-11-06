import unittest
from Lab1 import TaskComplition

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = TaskComplition()

    #unit test of adding two numbers
    def test_add(self):
        self.assertEqual(self.calculator.add(5,5), 10)

    #unit test of substracting two numbers
    def test_substract(self):
        self.assertEqual(self.calculator.subtract(10,3), 7)
