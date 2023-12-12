# LabMenu7.py

from colorama import init
from labs.Shared.SaveFormats.save_formats import save_in_format
from labs.classes.Lab7.menu_utils import MenuUtils
import sys

init(autoreset=True)
DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/Data/Lab7/'

class MenuLab7:
    def __init__(self):
        self.saver = save_in_format()

    def display_format_choice(self, breeds):
        color = MenuUtils.choose_color()
        format_choice = MenuUtils.choose_display_format()

        if format_choice == "1":
            print("Displaying table...")
            MenuUtils.display_table(breeds, color)
        elif format_choice == "2":
            print("Displaying list...")
            MenuUtils.display_list(breeds, color)

    def save_data(self, breeds):
        MenuUtils.save_data(self.saver, breeds)

    def main(self):
        while True:
            user_option = MenuUtils.start_menu()

            if user_option == "1":
                breeds = MenuUtils.fetch_dog_breeds()
                self.display_format_choice(breeds)
                self.save_data(breeds)

                repeat_choice = input("Do you want to perform another operation? (y/n): ")
                if repeat_choice.lower() != 'y':
                    break
            elif user_option == "2":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please enter 1 or 2.")
