from colorama import Fore, Style
from labs.classes.Lab4.fonts import *
from labs.Shared.saveASCIIArt.SaveASCIIArt import save_ascii

class AsciiArtGenerator:
    DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab4/'
    def __init__(self):
        self.fonts = {
            "standard": standard_dic,
            "starwars": starwars_dic,
            "avatar": avatar_dic,
            "binary": standard_bin_dic
        }
        self.colors = [Fore.BLACK, Fore.RED, Fore.BLUE, Fore.YELLOW]
        self.save_ascii_handler = save_ascii()

    def generate_ascii_art(self, text, font_choice, color_choice):
        selected_font = list(self.fonts.values())[font_choice]
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
        return self.colors[color_choice] + ascii_art + Style.RESET_ALL

    def ask_save_ascii_art(self, ascii_text):
        self.save_ascii_handler.ask_save_ascii_art(ascii_text, self.DataPath)