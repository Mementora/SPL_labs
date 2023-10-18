
class ConsoleCalculator:
    def __init__(self, calculator):
        self.calculator = calculator

    def run(self):
        self.user_interface()

    def user_interface(self):
        print("Warning: if you want to use square root funtion it will return only the first number you "
              "entered")
        while True:
            print("press 1 to calculate")
            print("press q to exit")
            user_choice = input()
            if user_choice == '1':
                result = self.calculator.perform_calculation()
                print(f"result: {result}")
                print("repeat calculation? (y or n): ")
                user_choice = input()
                if user_choice != 'y':
                    break
            elif user_choice == 'q':
                return 1
