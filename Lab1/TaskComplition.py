from math import sqrt

# Task 9: global variable for using
archiveExpression = []
decimalNumber = 2

def main_menu():
    print("Welcome! if you want to use the calculator, press 1")
    print("If you want to see archived expressions, press 2")
    print("If you want to customize this app, press 3: ")
    userInput = input()
    if userInput == '1':
        user_input()
    elif userInput == '2':
        show_archived_expressions()
    elif userInput == '3':
        show_settings()

# Task 1: User input
# Task 3: Calculation
# Task 6: Decimal number
# Task 7: additional operations

def user_input():
    firstInput = float(input("Enter the first number: "))
    secondInput = float(input("Enter the second number: "))
    operator = input("Enter the operator symbol: ")
    error_handler(firstInput, secondInput, operator)
    check_correct_operator(operator)
    start_calculation(firstInput, secondInput, operator)

def start_calculation(num1, num2, operator):
    result = 0
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        if num2 == 0:
            print("Error: Can't divide by zero")
            recursive_calculation()
            return
        result = divide(num1, num2)
    elif operator == '^':
        result = pow(num1, num2)
    elif operator == 'sqrt':
        userChoice = int(input("This operator requires only one number. Press 1 or 2 for the needed number: "))
        if userChoice == 1:
            result = square_root(num1)
        elif userChoice == 2:
            result = square_root(num2)
        else:
            print("Wrong answer. You can only choose number one or two")
            recursive_calculation()
            return
    elif operator == '%':
        result = remainder(num1, num2)
    else:
        print("Invalid operator entered, please try again")
        recursive_calculation()
        return

    print(f"{num1} {operator} {num2} = {result}")
    archive_expression(num1, operator, num2, result)

def add(num1, num2):
    return float(num1 + num2)

def subtract(num1, num2):
    return float(num1 - num2)

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return float(num1 * num2)

def square_root(num1, num2):
    return float(sqrt(num1))

def power(num1, num2):
    return float(pow(num1, num2))

def remainder(num1, num2):
    return num1 % num2


# Task 2: Operator verification
def check_correct_operator(o):
    operators = ['+', '-', '*', '/', '^', 'sqrt', '%']
    if o not in operators:
        print("Invalid operator entered, please try again")
        user_input()


# Task 4:Repetition of calculations
def recursive_calculation():
    answer = input("Repeat the calculation? (y or n)")
    if answer == 'y':
        user_input()
    elif answer == 'n':
        main_menu()
    else:
        print("Error: No such option. Please select y or n")
        recursive_calculation()


# Task 5: Error Handler
def error_handler(numOne, numTwo, op):
    if (numOne == 0) | (numTwo == 0) & (op == '/'):
        print("Error: can't divide by zero")
        recursive_calculation()


# Task 8: Result archive
# Task 9: Expression archive
def archive_expression(firstNumber, operator, secondNumber, result):
    expressionTemplate = f"{firstNumber} {operator} {secondNumber} = {result}"
    userAnswer = input("Do you want to save expression? (y or n)")
    if userAnswer == 'y':
        archiveExpression.append(expressionTemplate)
        recursive_calculation()
    if userAnswer == 'n':
        recursive_calculation()


def show_archived_expressions():
    if len(archiveExpression) == 0:
        print("Archive is empty!")
        main_menu()
    for savedExpressions in archiveExpression:
        print(savedExpressions)
    main_menu()

# Task 10: user customization
def show_settings():
    global decimalNumber
    print("if you want to delete archive of expressions press 1")
    print("змінити заокруглення натисніть 2: ")
    userInput = input()
    if userInput == '1':
        archiveExpression.clear()
        main_menu()
    elif userInput == '2':
        decimalNumber = int(input("введіть потрібне число: "))
        if ((decimalNumber > 10) or (decimalNumber < 0)):
            print("Incorrect number! Enter valid")
        else:
            print("заокруглення пройшло успішно")
            main_menu()