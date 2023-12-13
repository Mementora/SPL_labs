from math import sqrt
def add(self, num1, num2):
    return float(num1 + num2)

class CalculatorOperations:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return float(num1 + num2)

    def subtract(self, num1, num2):
        return float(num1 - num2)

    def divide(self, num1, num2):
        return num1 / num2

    def multiply(self, num1, num2):
        return float(num1 * num2)

    def square_root(self, num):
        return float(sqrt(num))

    def power(self, num1, num2):
        return float(pow(num1, num2))

    def remainder(self, num1, num2):
        return num1 % num2