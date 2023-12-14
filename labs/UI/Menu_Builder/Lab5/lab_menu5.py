from labs.classes.Lab5.console_rectangle import ConsoleRectangle
import os

class ConsoleInterface:
    DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab5/'

    def __init__(self):
        pass

    def run(self):
        self.print_interface()

    def print_interface(self):
        rectangle = ConsoleRectangle()

        print("If you want to draw a rectangle, press 1:")
        print("If you want to exit, press f:")
        user_choice = input()

        if user_choice == '1':
            rectangle.run()
            self.save_object(rectangle)
        elif user_choice == 'f':
            return 1

    def save_object(self, rectangle):
        filename = input("Enter the filename to save the object: ")
        file_path = os.path.join(self.DataPath, filename + ".txt")

        # Specify the filename when saving the object
        rectangle.save_object(file_path)

# Example usage:
# console_interface = ConsoleInterface()
# console_interface.run()
