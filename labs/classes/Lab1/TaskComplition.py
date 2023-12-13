from math import sqrt
from labs.Shared.CalcOperations.CalcOp import CalculatorOperations

class Calculator:
    def __init__(self):
        self.archiveExpression = []
        self.decimalNumber = 2

    def main_menu(self):
        print("Welcome! If you want to use the calculator, press 1")
        print("If you want to see archived expressions, press 2")
        print("If you want to customize this app, press 3: ")
        userInput = input()
        if userInput == '1':
            self.user_input()
        elif userInput == '2':
            self.show_archived_expressions()
        elif userInput == '3':
            self.show_settings()

    def user_input(self):
        firstInput = float(input("Enter the first number: "))
        secondInput = float(input("Enter the second number: "))
        operator = input("Enter the operator symbol: ")
        self.error_handler(firstInput, secondInput, operator)
        self.check_correct_operator(operator)
        self.start_calculation(firstInput, secondInput, operator)

    def start_calculation(self, num1, num2, operator):
        result = 0
        if operator == '+':
            result = self.add(num1, num2)
        elif operator == '-':
            result = self.subtract(num1, num2)
        elif operator == '*':
            result = self.multiply(num1, num2)
        elif operator == '/':
            if num2 == 0:
                print("Error: Can't divide by zero")
                self.recursive_calculation()
                return
            result = self.divide(num1, num2)
        elif operator == '^':
            result = self.power(num1, num2)
        elif operator == 'sqrt':
            userChoice = int(input("This operator requires only one number. Press 1 or 2 for the needed number: "))
            if userChoice == 1:
                result = self.square_root(num1)
            elif userChoice == 2:
                result = self.square_root(num2)
            else:
                print("Wrong answer. You can only choose number one or two")
                self.recursive_calculation()
                return
        elif operator == '%':
            result = self.remainder(num1, num2)
        else:
            print("Invalid operator entered, please try again")
            self.recursive_calculation()
            return

        print(f"{num1} {operator} {num2} = {result}")
        self.archive_expression(num1, operator, num2, result)

    def check_correct_operator(self, o):
        operators = ['+', '-', '*', '/', '^', 'sqrt', '%']
        if o not in operators:
            print("Invalid operator entered, please try again")
            self.user_input()

    def recursive_calculation(self):
        answer = input("Repeat the calculation? (y or n)")
        if answer == 'y':
            self.user_input()
        elif answer == 'n':
            self.main_menu()
        else:
            print("Error: No such option. Please select y or n")
            self.recursive_calculation()

    def error_handler(self, numOne, numTwo, op):
        if (numOne == 0 or numTwo == 0) and op == '/':
            print("Error: can't divide by zero")
            self.recursive_calculation()

    def archive_expression(self, firstNumber, operator, secondNumber, result):
        expressionTemplate = f"{firstNumber} {operator} {secondNumber} = {result}"
        userAnswer = input("Do you want to save expression? (y or n)")
        if userAnswer == 'y':
            self.archiveExpression.append(expressionTemplate)
            self.recursive_calculation()
        if userAnswer == 'n':
            self.recursive_calculation()

    def show_archived_expressions(self):
        if len(self.archiveExpression) == 0:
            print("Archive is empty!")
            self.main_menu()
        for savedExpressions in self.archiveExpression:
            print(savedExpressions)
        self.main_menu()

    def show_settings(self):
        print("if you want to delete archive of expressions press 1")
        print("Change rounding by pressing 2: ")
        userInput = input()
        if userInput == '1':
            self.archiveExpression.clear()
            self.main_menu()
        elif userInput == '2':
            self.decimalNumber = int(input("Enter the desired number: "))
            if not 0 <= self.decimalNumber <= 10:
                print("Incorrect number! Enter a valid number between 0 and 10.")
            else:
                print("Rounding successful")
                self.main_menu()