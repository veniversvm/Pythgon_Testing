import unittest
from unittest.mock import patch
from src.api_client import get_location

class ApiClienteTest(unittest.TestCase):


    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'country': 'United States', 'regionName': 'California', 'cityName': 'Mountain View', 'countryName': 'United States'}
        result = get_location("8.8.8.8")
        self.assertEqual(result, {'country': 'United States', 'region': 'California', 'city': 'Mountain View', }, "no equal data")
        # confirma que el metodo solo se llamo una vez
        mock_get.assert_called_once_with(f"https://freeipapi.com/api/json/8.8.8.8")