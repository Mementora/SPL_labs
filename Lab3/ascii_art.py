from pyfiglet import Figlet

class ascii_art_convertor:
    def __init__(self):
        self.text = None

    def create_ascii_art(self, text):
        f = Figlet(font = 'starwars')
        print(f.renderText(text))