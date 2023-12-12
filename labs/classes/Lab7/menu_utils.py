from colorama import Fore
from tabulate import tabulate
from labs.classes.Lab7.display_dog_api import DisplayDogApi

class MenuUtils:

    @staticmethod
    def display_table(data, color):
        headers = [Fore.RESET + color + "Dog Breed", Fore.RESET + color + "PictureUrl"]
        rows = [(color + breed, DisplayDogApi.get_random_image(breed)) for breed in data]
        print(tabulate(rows, headers, tablefmt="grid"))

    @staticmethod
    def display_list(data, color):
        for breed in data:
            print(color + f"{breed}: {DisplayDogApi.get_random_image(breed)}")

    @staticmethod
    def choose_display_format():
        while True:
            print("Choose a display format:")
            print("1. Table")
            print("2. List")
            format_choice = input("Enter the number of the display format: ")

            if format_choice in ("1", "2"):
                return format_choice
            else:
                print("Invalid display format. Please enter 1 or 2.")

    @staticmethod
    def choose_color():
        while True:
            print("Choose a color:")
            print("1. Red")
            print("2. Green")
            print("3. Yellow")
            color_choice = input("Enter the number of the color: ")

            if color_choice == "1":
                return Fore.RED
            elif color_choice == "2":
                return Fore.GREEN
            elif color_choice == "3":
                return Fore.YELLOW
            else:
                print("Invalid color choice. Please enter 1, 2, or 3.")

    @staticmethod
    def start_menu():
        print("Hello! Choose the option:")
        print("1. Continue")
        print("2. Exit")
        option = input("Enter the number of the option: ")
        return option

    @staticmethod
    def fetch_dog_breeds():
        print("Fetching dog breeds...")
        breeds = DisplayDogApi.get_all_breeds()
        print(f"Received {len(breeds)} breeds.")
        return breeds

    @staticmethod
    def save_data(saver,DataPath, breeds):
        save_choice = input("Do you want to save the data? (y/n): ")
        if save_choice.lower() == 'y':
            save_format = input("Choose a save format:\n1. JSON\n2. CSV\n3. TXT\nEnter the number of the save format: ")
            save_filename = input("Enter the filename: ")
            if save_format == "1":
                saver.save_to_json(breeds, DataPath, save_filename)
            elif save_format == "2":
                saver.save_to_csv(breeds, DataPath, save_filename)
            elif save_format == "3":
                saver.save_to_txt(breeds, DataPath, save_filename)
            else:
                print("Invalid save format. Please enter 1, 2, or 3.")