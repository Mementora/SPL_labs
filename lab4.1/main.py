import Console


if __name__ == '__main__':
    console_app = Console.Console()
    user_input, selected_font, selected_color, width, height, char_set, preview_enabled = console_app.get_user_input()
    ascii_text =

    if preview_enabled == 'y':
        console_app.preview_ascii_art(ascii_text, selected_color)

    save_confirmation = input("Save ASCII art to a file? (y/n): ").strip().lower()
    if save_confirmation == 'y':
        file_name = input("Enter a file name to save the ASCII art (without extension): ")
        console_app.save_ascii_art(ascii_text, file_name)
