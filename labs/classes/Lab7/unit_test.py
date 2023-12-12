import unittest
from unittest.mock import patch, MagicMock
from display_dog_api import DisplayDogApi
from labs.UI.Menu_Builder.Lab7.LabMenu7 import MenuLab7

class TestDisplayDogApi(unittest.TestCase):
    @patch('requests.get')
    def test_get_all_breeds(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": {"breed1": {}, "breed2": {}}}
        mock_requests_get.return_value = mock_response

        breeds = DisplayDogApi.get_all_breeds()

        self.assertEqual(list(breeds), ["breed1", "breed2"])

    @patch('builtins.input', side_effect=['3'])
    def test_invalid_display_format(self):
        with self.assertRaises((ValueError, StopIteration)):
            MenuLab7.choose_display_format()