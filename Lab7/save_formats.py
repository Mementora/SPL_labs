import json, csv
import os

from colorama import Fore, init
from display_dog_api import DisplayDogApi

class save_in_format:
    def __init__(self):
        pass

    def remove_color_codes(self, text):
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text

    def save_to_json(self, data, directory, filename):
        filepath = os.path.join(directory, filename)

        data_to_save = [{"DogBreed": breed, "PictureUrl": DisplayDogApi.get_random_image(breed)} for breed in data]
        with open(filepath, 'w') as file:
            json.dump(data_to_save, file, indent=2)
        print(f"Data saved to {filepath} in JSON format.")

    def save_to_csv(self, data, directory, filename):
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Fore.RESET + "DogBreed", Fore.RESET + "PictureUrl"])
            for breed in data:
                writer.writerow(
                    [self.remove_color_codes(breed), self.remove_color_codes(DisplayDogApi.get_random_image(breed))])
        print(f"Data saved to {filepath} in CSV format.")

    def save_to_txt(self, data, directory, filename):
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w') as file:
            for breed in data:
                file.write(
                    f"{self.remove_color_codes(breed)}: {self.remove_color_codes(DisplayDogApi.get_random_image(breed))}\n")
        print(f"Data saved to {filepath} in TXT format.")