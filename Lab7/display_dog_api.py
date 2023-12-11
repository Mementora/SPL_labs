import requests

class DisplayDogApi:
    BASE_URL = "https://dog.ceo/api"

    @classmethod
    def get_all_breeds(cls):
        response = requests.get(f"{cls.BASE_URL}/breeds/list/all")
        data = response.json()
        breeds = data.get("message", {})
        return breeds.keys()

    @classmethod
    def get_random_image(cls, breed):
        response = requests.get(f"{cls.BASE_URL}/breed/{breed}/images/random")
        data = response.json()
        image_url = data.get("message", "")
        return image_url