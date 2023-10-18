from pyfiglet import Figlet
from colorama import Fore, Style


class ascii_art_convertor:
        def __init__(self):
            self.text = None

        def perform_ascii_covnentor(self, text, font, color):
            return self.create_ascii_art(text, font, color)

        def create_ascii_art(self, text, font, color):
            f = Figlet(font=font)
            print(color + Style.BRIGHT + f.renderText(text))

