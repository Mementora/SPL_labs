import requests
from unittest.mock import patch, MagicMock

class DisplayDogApi:
    @staticmethod
    @patch('requests.get')
    def get_all_breeds(mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": {"breed1": {}, "breed2": {}}}
        mock_requests_get.return_value = mock_response
        breeds = DisplayDogApi.get_all_breeds()
        return list(breeds)

        @classmethod
        def get_random_image(cls, breed):
            response = requests.get(f"{cls.BASE_URL}/breed/{breed}/images/random")
            data = response.json()
            image_url = data.get("message", "")
            return image_url