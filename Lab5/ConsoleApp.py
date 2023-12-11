from ConsoleRectangle import ConsoleRectangle

class ConsoleInterface:
    def __init__(self):
        pass

    def run(self):
        self.print_interface()

    def print_interface(self):
        rectangle = ConsoleRectangle()

        print("if you want to draw rectangle, press 1: ")
        print("if you want to exit, press f:")
        user_choice = input()
        if user_choice == '1':
            rectangle.run()
        elif user_choice == 'f':
            return 1

