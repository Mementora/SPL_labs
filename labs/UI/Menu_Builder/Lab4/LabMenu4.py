from colorama import Fore, Style

class LabMenu4:
    def __init__(self, ascii_art_generator):
        self.ascii_art_generator = ascii_art_generator

    def run(self):
        user_input, font_choice, color_choice = self.get_user_input()
        ascii_text = self.ascii_art_generator.generate_ascii_art(user_input, font_choice, color_choice)
        self.preview_ascii_art(ascii_text, self.ascii_art_generator.colors[color_choice])

        save_option = input("Do you want to save the ASCII art to a file? (y/n): ")
        if save_option.lower() == 'y':
            file_name = input("Enter the file name (without extension): ")
            self.ascii_art_generator.save_ascii_art(ascii_text, file_name)

    def get_user_input(self):
        user_input = input("Enter a word to convert to ASCII art: ")

        self.show_available_fonts()
        font_choice = self.get_font_choice()

        self.show_available_colors()
        color_choice = self.get_color_choice()

        return user_input, font_choice, color_choice

    def show_available_fonts(self):
        print("Available Fonts:")
        for font_name in self.ascii_art_generator.fonts.keys():
            print(f" - {font_name}")

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
        print("Available Colors:")
        for i, color in enumerate(self.ascii_art_generator.colors):
            print(f"{i} - {color}")

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
