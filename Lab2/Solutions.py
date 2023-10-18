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
        self.start_calculation()

    def perform_calculation(self):
        self.user_input()
        return self.start_calculation()

    def start_calculation(self):
        if self.operator == '+':
            return self.add()
        elif self.operator == '-':
            return self.subtract()
        elif self.operator == '*':
            return self.multiply()
        elif self.operator == '/':
            return self.divide()
        elif self.operator == 'sqrt':
            return self.square_root()

        elif self.operator == '^':
            return self.power()
        elif self.operator == '%':
            return self.remainder()
        else:
            return "Invalid operator"

    def check_input(self):
        if self.first_input == '' or self.second_input == '':
            return "Empty input"
        if (self.first_input == 0 or self.second_input == 0) and self.operator == '/':
            return "can't divide by zero"

    def add(self):
        result = float(self.first_input + self.second_input)
        return result

    def subtract(self):
        result = float(self.first_input - self.second_input)
        return result

    def divide(self):
        result = self.first_input / self.second_input
        return result

    def multiply(self):
        result = float(self.first_input * self.second_input)
        return result

    def square_root(self):
        result = float(sqrt(self.first_input))
        return result

    def power(self):
        result = float(pow(self.first_input, self.second_input))
        return result

    def remainder(self):
        result = self.first_input % self.second_input
        return result

    def repeat_calculation(self):
        self.user_input()
