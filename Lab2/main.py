from Solutions import Calculator
from ConsoleApp import ConsoleCalculator

if __name__ == '__main__':
    calc = Calculator()
    console_calculation = ConsoleCalculator(calc)
    console_calculation.run()
