import os

class save_ascii:
    def __init__(self):
        pass

    def ask_save_ascii_art(self, ascii_text, DataPath):
        try:
            save_option = input("Do you want to save the ASCII art to a file? (y/n): ").strip().lower()
            if save_option != 'y':
                print("ASCII art not saved.")
                return

            file_name = input("Enter the desired file name (e.g., art.txt): ").strip()

            # Construct the file path using DataPath
            file_path = os.path.join(DataPath, f"{file_name}.txt")

            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the directory exists

            # Assuming you have a generator attribute in your class, adjust accordingly
            # self.generator.save_ascii_art(ascii_text, file_path)
            with open(file_path, 'w') as file:
                file.write(ascii_text)

            print(f"ASCII art saved to {file_path}")

        except Exception as e:
            print(f"Error saving ASCII art: {e}")
