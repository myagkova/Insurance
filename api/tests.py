# import pytest
from django.test import TestCase, Client
from .apps import ApiConfig


class TestPredictionAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = ApiConfig.model
        cls.client = Client()

    def test_incorrect_requ(self):
        data = {'Age': 20, 'Driving_experience': 1, 'Salary': 700}
        response = client.get(
            "/AddMessage",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        self.assertEqual(response.status_code, 200)
