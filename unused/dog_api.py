class DogAPI:
    base_url = "https://api.thedogapi.com/v1"

    def __init__(self, api_key):
        self.headers = {"x-api-key": api_key}
