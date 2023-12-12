from colorama import Fore, Style
from labs.classes.Lab3.ASCIIArtGenerator import ASCIIArtGenerator
import os

class LabMenu3:
    DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab3/'
    def __init__(self):
        self.colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.BLACK]
        self.generator = ASCIIArtGenerator()

    def get_user_input(self):
        user_input = input("Enter a word or phrase to convert to ASCII art: ")

        self.show_available_fonts()
        font_choice = self.get_font_choice()

        self.show_available_colors()
        color_choice = self.get_color_choice()

        width = self.get_positive_number("Enter the width of the ASCII art (number of characters in a line): ")
        height = self.get_positive_number("Enter the height of the ASCII art (number of lines): ")

        use_custom_chars = input("Do you want to choose a special character to create ASCII art? (y/n): ").strip().lower()
        char_set = self.get_custom_characters() if use_custom_chars == 'y' else None

        preview_enabled = input("Want to preview your ASCII art before saving? (y/n): ").strip().lower()

        return user_input, self.generator.fonts[font_choice - 1], self.colors[color_choice - 1], width, height, char_set, preview_enabled

    def show_available_fonts(self):
        print("Available font styles:")
        for i, font in enumerate(self.generator.fonts, start=1):
            print(f"{i}. {font}")

    def get_font_choice(self):
        while True:
            try:
                font_choice = int(input("Choose a font style number (1-4): "))
                if 1 <= font_choice <= 4:
                    return font_choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter the correct font style number.")

    def show_available_colors(self):
        print("Available text colors:")
        for i, color in enumerate(self.colors, start=1):
            print(f"{i}. Color {color}")

    def get_color_choice(self):
        while True:
            try:
                color_choice = int(input(Fore.RESET + "Choose a text color number (1-4): "))
                if 1 <= color_choice <= 4:
                    return color_choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter the correct text color number.")

    def get_positive_number(self, prompt):
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number
                else:
                    print("Please enter a number greater than zero.")
            except ValueError:
                print("Please enter the correct number.")

    def get_custom_characters(self):
        return input("Enter the characters you want to use for ASCII art (e.g., '@#*'): ")

    def preview_ascii_art(self, ascii_text, selected_color):
        print(selected_color + ascii_text + Style.RESET_ALL)

    def generate_ascii_art(self, text, selected_font, selected_color, width, height, char_set=None):
        ascii_text = self.generator.generate_ascii_art(text, selected_font, width, height, char_set)
        colored_text = selected_color + ascii_text + Style.RESET_ALL
        return colored_text

    def ask_save_ascii_art(self, ascii_text):
        save_option = input("Do you want to save the ASCII art to a file? (y/n): ").strip().lower()
        if save_option != 'y':
            print("ASCII art not saved.")
            return

        file_name = input("Enter the desired file name (e.g., art.txt): ").strip()

        # Construct the file path using DataPath
        file_path = os.path.join(self.DataPath, f"{file_name}")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the directory exists

        self.generator.save_ascii_art(ascii_text, file_path)
        print(f"ASCII art saved to {file_path}")