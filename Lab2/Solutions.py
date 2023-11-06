from math import sqrt

class Calculator:
    def __init__(self):
        self.first_input = None
        self.second_input = None
        self.operator = None

    def user_input(self):
        self.first_input = float(input("enter the first number: "))
        self.second_input = float(input("enter the second number: "))
        self.operator = input("enter operator (+,-,*,/,sqrt,^,%): ")
        self.check_input()
        result = self.start_calculation()
        print("Result:", result)

    def check_input(self):
        if self.first_input == '' or self.second_input == '':
            return "Empty input"
        if (self.first_input == 0 or self.second_input == 0) and self.operator == '/':
            return "Can't divide by zero"

    def start_calculation(self):
        if self.operator == '+':
            return self.add(self.first_input, self.second_input)
        elif self.operator == '-':
            return self.subtract(self.first_input, self.second_input)
        elif self.operator == '*':
            return self.multiply(self.first_input, self.second_input)
        elif self.operator == '/':
            return self.divide(self.first_input, self.second_input)
        elif self.operator == 'sqrt':
            return self.square_root(self.first_input)
        elif self.operator == '^':
            return self.power(self.first_input, self.second_input)
        elif self.operator == '%':
            return self.remainder(self.first_input, self.second_input)
        else:
            return "Invalid operator"

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        if num1 == 0 or num2 == 0:
            return "Can't divide by zero"
        return num1 / num2

    def multiply(self, num1, num2):
        return num1 * num2

    def square_root(self, num1):
        if num1 < 0:
            return "Cannot take the square root of a negative number"
        return sqrt(num1)

    def power(self, num1, num2):
        return num1 ** num2

    def remainder(self, num1, num2):
        if num2 == 0:
            return "Can't find the remainder when dividing by zero"
        return num1 % num2

    def repeat_calculation(self):
        self.user_input()
