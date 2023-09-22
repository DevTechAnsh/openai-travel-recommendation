import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


class TestRecommendations(unittest.TestCase):
    def setUp(self):
        self.country = "usa"
        self.season = "summer"
        self.client = TestClient(app)

    # use the @patch decorator to mock the recommend_activities function
    @patch("api.activity.recommend_activities")
    def test_get_recommendations_with_valid_args(self, mock_call_openai_gpt_api):
        # mock the gpt function

        mock_call_openai_gpt_api.return_value = "Mocked recommendations from OpenAI GPT"
        # Send a request to the endpoint
        response = self.client.get(f'/?country={self.country}&season={self.season}')
        
        # check the status code is 200
        self.assertEqual(response.status_code, 200)

        expected_response = {
            "country": "usa",
            "season": "summer",
            "recommendations": "Mocked recommendations from OpenAI GPT",
        }
        self.assertEqual(response.json(), expected_response)
        # Assert recommend_activities with the expected arguments
        mock_call_openai_gpt_api.assert_called_once_with(self.country, self.season)

    @patch("api.activity.recommend_activities")
    def test_get_recommendations_with_empty_season(self, mock_call_openai_gpt_api):
        # mock the gpt function
        mock_call_openai_gpt_api.return_value = "Mocked recommendations from OpenAI GPT"

        # Send a request to the endpoint
        response = self.client.get(f"/?country={self.country}&season=''")

        # check the status code is 400
        self.assertEqual(response.status_code, 400)

        expected_response = {
            "detail": "Invalid season. Allowed seasons are spring, summer, rainy, and winter."}
        self.assertEqual(response.json(), expected_response)

    @patch("api.activity.recommend_activities")
    def test_get_recommendations_with_empty_country(self, mock_call_openai_gpt_api):
        # mock the gpt function
        mock_call_openai_gpt_api.return_value = "Mocked recommendations from OpenAI GPT"

        # Send a request to the endpoint
        response = self.client.get(f"/?country=&season={self.season}")
        # check the status code is 422
        self.assertEqual(response.status_code, 422)
