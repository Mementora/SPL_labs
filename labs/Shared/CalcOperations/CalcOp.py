import logging
from math import sqrt
from datetime import datetime

log_file_path = "/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/logger/logger.log"

class CalculatorOperations:
    def __init__(self):
        # Configure logging
        logging.basicConfig(filename=log_file_path, level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def log_operation(self, operation_name, result):
        self.logger.info(f"{operation_name} operation. Result: {result}. Date: {datetime.now()}")

    def add(self, num1, num2):
        result = float(num1 + num2)
        self.log_operation("Adding", result)
        return result

    def subtract(self, num1, num2):
        result = float(num1 - num2)
        self.log_operation("Subtracting", result)
        return result

    def divide(self, num1, num2):
        try:
            result = num1 / num2
            self.log_operation("Dividing", result)
            return result
        except ZeroDivisionError:
            self.logger.error("Division by zero is not allowed.")
            return None

    def multiply(self, num1, num2):
        result = float(num1 * num2)
        self.log_operation("Multiplying", result)
        return result

    def square_root(self, num):
        if num < 0:
            self.logger.error("Square root of a negative number is undefined.")
            return None
        result = float(sqrt(num))
        self.log_operation("Calculating square root", result)
        return result

    def power(self, num1, num2):
        result = float(pow(num1, num2))
        self.log_operation("Power", result)
        return result

    def remainder(self, num1, num2):
        result = num1 % num2
        self.log_operation("Calculating remainder", result)
        return result
