
#issue: func doing job twice
class Console_calculator:
    def __init__(self, calculator):
        self.calculator = calculator

    def run(self):
        self.user_interface()

    def user_interface(self):
        print("press 1 to calculate")
        print("press q to exit")
        user_choice = input()
        if user_choice == '1':
            user_choice == ''
            result = self.calculator.perform_calculation()
            print(f"result: {result}")
            print("repeat calculation? (y or n): ")
            user_choice = input()
            if user_choice == 'y':
                self.calculator.repeat_calculation()
            elif user_choice == 'n':
                self.user_interface()
        elif user_choice == 'q':
            return 1
