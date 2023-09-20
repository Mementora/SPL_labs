from math import sqrt

# Task 9: global variable for using
archiveExpression = []
decimalNumber = 2

def main_menu():
    print("Welcome! if you want to use calculator press 1")
    print("if you want to see archived expressions press 2")
    print("if you want to customize this app, press 3: ")
    userInput = input()
    if userInput == '1':
        arithmetic_calculator()
    elif userInput == '2':
        show_archived_expressions()
    elif userInput == '3':
        show_settings()


# Task 1: User input
# Task 3: Calculation
# Task 6: Decimal number
# Task 7: additional operations
def arithmetic_calculator():
    firstInput = float(input("Enter the first number: "))
    secondInput = float(input("Enter the second number: "))
    operator = input("Enter the operator symbol: ")
    result = 0

    error_handler(firstInput, secondInput, operator)
    check_correct_operator(operator)

    if operator == '+':
        result = firstInput + secondInput
    elif operator == '-':
        result = firstInput - secondInput
    elif operator == '*':
        result = firstInput * secondInput
    elif operator == '/':
        result = firstInput / secondInput
    elif operator == '^':
        result = pow(firstInput, secondInput)
    elif operator == 'sqrt':
        userChoice = int(input("this operator requires only one number. Press 1 or 2 for needed number"))
        if userChoice == 1:
            result = sqrt(firstInput)
            print(result)
        elif userChoice == 2:
            result = sqrt(secondInput)
            print(result)
        else:
            print("Wrong answer. You can only choose number one or two")
        recursive_calculation()
    elif operator == '%':
        result = firstInput % secondInput

    print(f"{firstInput} {operator} {secondInput} = {result}")

    if decimalNumber == 0:
        result = round(result, decimalNumber)
    else:
        result = int(round(result))
    print(result)
    archive_expression(firstInput, operator, secondInput, result)
    recursive_calculation()


# Task 2: Operator verification
def check_correct_operator(o):
    operators = ['+', '-', '*', '/', '^', 'sqrt', '%']
    if o not in operators:
        print("Invalid operator entered, please try again")
        arithmetic_calculator()


# Task 4:Repetition of calculations
def recursive_calculation():
    answer = input("Repeat the calculation? (y or n)")
    if answer == 'y':
        arithmetic_calculator()
        recursive_calculation()
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
        arithmetic_calculator()
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
            arithmetic_calculator()
