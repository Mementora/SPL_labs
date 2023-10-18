from pyfiglet import Figlet
from colorama import Fore, Style


class ConsoleApp:

    def __init__(self, ascii):
        self.ascii = ascii
        self.choosed_color = Fore.RESET
        self.current_font = 'standard'

    def run(self):
        self.user_interface()

    def user_interface(self):
        while True:
                text = input(Fore.RESET + "enter text: ")
                font = self.set_ascii_font()
                color = self.set_ascii_color()
                self.ascii.perform_ascii_covnentor(text, font, color)

    # set font for generated ascii art
    def set_ascii_font(self):
        available_fonts = ["standard", "banner", "slant", "starwars"]

        while True:
            print("Available font styles:")
            for i, font in enumerate(available_fonts, start=1):
                print(f"{i}. {font}")

            try:
                font_choice = int(input("Choose a font number (1-4): "))

                if 1 <= font_choice <= len(available_fonts):
                    selected_font = available_fonts[font_choice - 1]
                    return selected_font
                else:
                    print("Please enter a correct number (1-4)")
            except ValueError:
                print("Please enter a font number (1-4)")

    # set color for generated ascii art
    def set_ascii_color(self):
        print(
            "Available text colors:\n" +
            Fore.LIGHTRED_EX + "1. Red\n"
            + Fore.LIGHTBLUE_EX + "2. Blue\n" +
            Fore.LIGHTGREEN_EX + "3. Green")

        while True:
            try:
                color_choice = int(input(Fore.RESET + "choose from available options[1-3]"))
                if 1 <= color_choice <= 3:
                    break
                else:
                    print("invalid number, try again [1-3]")
            except ValueError:
                print("Enter correct color number [1-3]")

    def use_custom_char(self):
        custom_char = input("Do you want to choose a specific chracter to generate ASCII art? (y or n)")
        if custom_char == 'y':
            char_set = input("Enter the characters you want to use for ASCII art: ")
        else:
            char_set = None
