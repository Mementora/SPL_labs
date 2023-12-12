import pyfiglet

class ASCIIArtGenerator:
    def __init__(self):
        self.fonts = ['standard', 'banner', 'slant', 'starwars']

    def generate_ascii_art(self, text, selected_font, width, height, char_set=None):
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

        return scaled_ascii_text

    def save_ascii_art(self, ascii_text, file_name):
        with open(f"{file_name}.txt", "w") as file:
            file.write(ascii_text)
        print(f"ASCII art is saved in a file {file_name}")
