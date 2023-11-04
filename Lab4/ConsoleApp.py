from colorama import Fore, Style
import ascii_art_generator
class ConsoleApp:
    def __init__(self):

        self.fonts = ['standard', 'banner', 'slant', 'starwars']
        self.colors = [Fore.WHITE, Fore.BLUE, Fore.GREEN, Fore.BLACK]

    def get_user_input(self):

        user_input = input("Enter a word or phrase to convert to ASCII art: ")

        self.show_available_fonts()
        font_choice = self.get_font_choice()

        self.show_available_colors()
        color_choice = self.get_color_choice()

        width = self.get_positive_number("Enter the width of the ASCII art (number of characters in a line): ")
        height = self.get_positive_number("Enter the height of the ASCII art (number of lines): ")

        char_set = self.get_custom_characters()

        preview_enabled = input("Want to preview your ASCII art before saving? (y/n): ").strip().lower()

        return user_input, self.fonts[font_choice - 1], self.colors[color_choice - 1], width, height, char_set, preview_enabled

    def show_available_fonts(self):
        print("Available font styles:")
        for i, font in enumerate(self.fonts, start=0):
            print(f"{i}. {font}")

        # get user choise of font

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

        # show a list of colors

    def show_available_colors(self):
        print("Available text colors:")
        for i, color in enumerate(self.colors, start=0):
            print(f"{i}. Color {color}")

        # get user choise of color

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

        # using for detecting negative number

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

        # get the user choise

    def get_custom_characters(self):
        return input("Enter the characters you want to use for ASCII art (e.g., '@#*'): ")

        # use to preview generated ASCII art

    def preview_ascii_art(self, ascii_text, selected_color):
        print(selected_color + ascii_text + Style.RESET_ALL)

    def generate_ascii_art(self,text, selected_font, selected_color, width, height, char_set=None):
        return ascii_art_generator.generate_ascii_art(text,selected_font,selected_color,width,height,char_set)

    def save_ascii_art(self, ascii_text, file_name):
        return ascii_art_generator.save_ascii_art(ascii_text, file_name)
