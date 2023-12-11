from ASCIIArtGenerator import AsciiArtGenerator
from Console import AsciiArtConsole

def main():
    ascii_art_generator = AsciiArtGenerator()
    ascii_art_console = AsciiArtConsole(ascii_art_generator)
    ascii_art_console.run()

if __name__ == "__main__":
    main()