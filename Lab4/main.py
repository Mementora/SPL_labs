from Console import Console

if __name__ == '__main__':
    console_app = Console()
    user_input, font_choice, color_choice = console_app.get_user_input()
    ascii_text = console_app.generate_ascii_art(user_input, font_choice, color_choice)

    preview_enabled = input("Want to preview your ASCII art before saving? (y/n): ").strip().lower()

    if preview_enabled == 'y':
        console_app.preview_ascii_art(ascii_text, console_app.colors[color_choice])

    save_confirmation = input("Save ASCII art to a file? (y/n): ").strip().lower()
    if save_confirmation == 'y':
        file_name = input("Enter a file name to save the ASCII art (without extension): ")
        console_app.save_ascii_art(ascii_text, file_name)
