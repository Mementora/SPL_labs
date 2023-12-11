import labs.UI.Menu_Builder.Lab2.LabMenu2 as menu2
import labs.classes.Lab2


class main:
    if __name__ == '__main__':
        print("if you want to open lab2, press 2:")
        user_choice = input()
        if user_choice == '2':
            calculator_instance = labs.classes.Lab2.Calculator()
            calculator = menu2.LabMenu2(calculator_instance)
            calculator.run()
