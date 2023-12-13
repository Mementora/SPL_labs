from labs.Shared.CalcOperations.CalcOp import CalculatorOperations

class Calculator:
    def __init__(self):
        self.first_input = None
        self.second_input = None
        self.operator = None
        self.calc_operations = CalculatorOperations()

    def perform_calculation(self):
        return self.start_calculation()

    def check_input(self):
        if self.first_input == '' or self.second_input == '':
            return "Empty input"
        if (self.first_input == 0 or self.second_input == 0) and self.operator == '/':
            return "Can't divide by zero"

    def start_calculation(self):
        if self.operator == '+':
            return self.calc_operations.add(self.first_input, self.second_input)
        elif self.operator == '-':
            return self.calc_operations.subtract(self.first_input, self.second_input)
        elif self.operator == '*':
            return self.calc_operations.multiply(self.first_input, self.second_input)
        elif self.operator == '/':
            return self.calc_operations.divide(self.first_input, self.second_input)
        elif self.operator == 'sqrt':
            return self.calc_operations.square_root(self.first_input)
        elif self.operator == '^':
            return self.calc_operations.power(self.first_input, self.second_input)
        elif self.operator == '%':
            return self.calc_operations.remainder(self.first_input, self.second_input)
        else:
            return "Invalid operator"
