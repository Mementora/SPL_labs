from colorama import Fore, Style
from fonts import *

class Console:
    def __init__(self):
        self.font = {
            "standart": standard_dic,
            "starwars": starwars_dic,
            "avatar": avatar_dic
        }
        self.colors = [Fore.BLACK, Fore.RED, Fore.BLUE, Fore.YELLOW]

    def get_user_input(self):
        user_input = input("Enter a word to convert to ASCII art: ")

        self.show_available_fonts()
        font_choice = self.get_color_choice()

        self.show_available_colors()
        color_choice = self.get_color_choice()

        char_set = self.get_custom_characters()

    def show_available_fonts(self):
        print("Available font styles:")
        for i, font in enumerate(self.fonts, start=0):
            print(f"{i}. {font}")

    def get_font_choice(self):
        while True:
            try:
                font_choice = int(input("Choose a font style number (0-3): "))
                if 0 <= font_choice <= 3:
                    return font_choice
                else:
                    print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Please enter the correct font style number.")

    def get_font_choice(self):
        while True:
            try:
                font_choice = int(input("Choose a font style number (0-3): "))
                if 0 <= font_choice <= 3:
                    return font_choice
                else:
                    print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Please enter the correct font style number.")

    def show_available_colors(self):
        print("Available text colors:")
        for i, color in enumerate(self.colors, start=0):
            print(f"{i}. Color {color}")

    def get_color_choice(self):
        while True:
            try:
                color_choice = int(input(Fore.RESET + "Choose a text color number (0-3): "))
                if 1 <= color_choice <= 3:
                    return color_choice
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Please enter the correct text color number.")