from pyfiglet import Figlet
from colorama import Fore, Style

class ascii_art_convertor:
    def __init__(self):
        self.text = None

    def perform_ascii_covnentor(self,text):
       return self.create_ascii_art(text)

    def create_ascii_art(self, text):
        f = Figlet(font = 'starwars')
        print(Fore.RED + Style.BRIGHT + f.renderText(text))