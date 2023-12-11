from labs.classes.Lab1.TaskComplition import Calculator
class LabMenu1:
    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        print("Welcome to the Calculator App!")
        while True:
            print("Choose an option:")
            print("1. Use Calculator")
            print("2. Exit")
            choice = input()

            if choice == '1':
                self.calculator.main_menu()
            elif choice == '2':
                print("Exiting Calculator App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
