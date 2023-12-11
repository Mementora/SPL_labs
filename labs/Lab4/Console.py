from colorama import Fore, Style
from fonts import *  # Import your fonts
class Console:
    def __init__(self):
        self.fonts = {
            "standard": standard_dic,
            "starwars": starwars_dic,
            "avatar": avatar_dic,
            "binary": standard_bin_dic
        }
        self.colors = [Fore.BLACK, Fore.RED, Fore.BLUE, Fore.YELLOW]

    def get_user_input(self):
        user_input = input("Enter a word to convert to ASCII art: ")

        self.show_available_fonts()
        font_choice = self.get_font_choice()

        self.show_available_colors()
        color_choice = self.get_color_choice()

        return user_input, font_choice, color_choice

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

    def show_available_colors(self):
        print("Available text colors:")
        for i, color in enumerate(self.colors, start=0):
            print(f"{i}. Color {color}")

    def get_color_choice(self):
        while True:
            try:
                color_choice = int(input(Fore.RESET + "Choose a text color number (0-3): "))
                if 0 <= color_choice <= 3:
                    return color_choice
                else:
                    print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Please enter the correct text color number.")

    def preview_ascii_art(self, ascii_text, selected_color):
        print(selected_color + ascii_text + Style.RESET_ALL)

    def generate_ascii_art(self, text, font_choice, color_choice):
        selected_font = list(self.fonts.values())[font_choice]
        # Assuming the text contains only letters and is in lowercase for the font dictionary
        ascii_art = ""
        for line in range(len(selected_font['a'].split('\n'))):
            for char in text:
                if char.isalpha():
                    if char in selected_font:
                        ascii_art += selected_font[char].split('\n')[line]
                    else:
                        ascii_art += " " * 5  # Default space if character is not available
                else:
                    ascii_art += "\n"  # Move to the next line for non-letter characters
            ascii_art += "\n"  # Move to the next line after completing a line of characters
        return ascii_art

    def save_ascii_art(self, ascii_text, file_name):
        with open(f"{file_name}.txt", "w") as file:
            file.write(ascii_text)
        print(f"ASCII art is saved in a file {file_name}.txt")
