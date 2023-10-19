import ConsoleApp

def main():
    app = ConsoleApp.ConsoleApp()
    user_input, selected_font, selected_color, width, height, char_set, preview_enabled = app.get_user_input()
    ascii_text = app.generate_ascii_art(user_input, selected_font, selected_color, width, height, char_set)

    if preview_enabled == 'y':
        app.preview_ascii_art(ascii_text, selected_color)

    save_confirmation = input("Want to save ASCII art to a file? (y/n): ").strip().lower()
    if save_confirmation == 'y':
        file_name = input("Enter a file name to save the ASCII art (without extension): ")
        app.save_ascii_art(ascii_text, file_name)

if __name__ == "__main__":
    main()
