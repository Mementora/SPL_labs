import unittest
from labs.classes.Lab6.CalculatorTest import CalculatorTester

class LabMenu6:
    def __init__(self):
        pass

    def run_tests(self):
        test_suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTester)

        # Specify the full path to save the test results text file
        file_path = "/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab6/test_results.txt"

        # Create a test runner with output to the specified file path
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                runner = unittest.TextTestRunner(stream=f, verbosity=2)
                runner.run(test_suite)
            print(f"Test results successfully saved to {file_path}")
        except Exception as e:
            print(f"Error: {e}")