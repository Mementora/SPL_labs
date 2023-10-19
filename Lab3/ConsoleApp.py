import pyfiglet
from colorama import Fore, Style

class ConsoleApp:
    def __init__(self):
        self.fonts = ['standard', 'banner', 'slant', 'starwars']
        self.colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.BLACK]

    #get user input
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

        return user_input, self.fonts[font_choice - 1], self.colors[color_choice - 1], width, height, char_set, preview_enabled

    #show a list of available
    def show_available_fonts(self):
        print("Available font styles:")
        for i, font in enumerate(self.fonts, start=0):
            print(f"{i}. {font}")

    #get user choise of font
    def get_font_choice(self):
        while True:
            try:
                font_choice = int(input("Choose a font style number (0-3): "))
                if 1 <= font_choice <= 4:
                    return font_choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter the correct font style number.")

    #show a list of colors
    def show_available_colors(self):
        print("Available text colors:")
        for i, color in enumerate(self.colors, start=0):
            print(f"{i}. Color {color}")

    #get user choise of color
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

    #using for detecting negative number
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

    #get the user choise
    def get_custom_characters(self):
        return input("Enter the characters you want to use for ASCII art (e.g., '@#*'): ")

    #use to preview generated ASCII art
    def preview_ascii_art(self, ascii_text, selected_color):
        print(selected_color + ascii_text + Style.RESET_ALL)

    #generate ASCII art
    def generate_ascii_art(self, text, selected_font, selected_color, width, height, char_set=None):
        ascii_art = pyfiglet.Figlet(font=selected_font)
        ascii_text = ascii_art.renderText(text)
        ascii_lines = ascii_text.split('\n')

        scaled_ascii_lines = []
        char_set_length = len(char_set) if char_set else 0
        for line in ascii_lines:
            scaled_line = ""
            for char in line:
                if char == ' ':
                    scaled_line += ' '
                else:
                    if char_set:
                        scaled_line += char_set[hash(char) % char_set_length]
                    else:
                        scaled_line += char
            scaled_ascii_lines.append(scaled_line.center(width)[:width])

        scaled_ascii_text = '\n'.join(scaled_ascii_lines[:height])

        colored_text = selected_color + scaled_ascii_text + Style.RESET_ALL
        return colored_text

    #save ASCII art in .txt
    def save_ascii_art(self, ascii_text, file_name):
        with open(f"{file_name}.txt", "w") as file:
            file.write(ascii_text)
        print(f"ASCII art is saved in a file {file_name}.txt")
