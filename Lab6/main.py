import CalculatorTest
import unittest

if __name__ == '__main__':
    # Load unit tests from CalculatorTest
    test_suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest.CalculatorTester)

    # Create a test runner with output to a file
    with open('test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(test_suite)
