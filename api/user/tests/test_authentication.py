from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from user.factories import UserFactory

class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')
        self.user = UserFactory()

    def test_authentication_succes(self):
        data = {
            'username': self.user.username,
            'password': '123456'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data.keys())

    def test_authentication_fail_on_incorrect_password(self):
        data = {
            'username': self.user.username,
            'password': '1234568910'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('non_field_errors' in response.data.keys())

    def test_authentication_fail_on_incorrect_username(self):
        data = {
            'username': 'incorrectuser',
            'password': '123456'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('non_field_errors' in response.data.keys())
