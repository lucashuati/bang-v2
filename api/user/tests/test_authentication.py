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

    def _test_authentication(self, data, status_code, response_message):
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status_code)
        self.assertTrue(response_message in response.data.keys())

    def test_authentication_succes(self):
        self._test_authentication(
            {
                'username': self.user.username,
                'password': '123456'
            },
            status.HTTP_200_OK,
            'token'
        )

    def test_authentication_fail_on_incorrect_password(self):
        self._test_authentication(
            {
                'username': self.user.username,
                'password': '1234568910'
            },
            status.HTTP_400_BAD_REQUEST,
            'non_field_errors'
        )

    def test_authentication_fail_on_incorrect_username(self):
        self._test_authentication(
            {
                'username': 'incorrectuser',
                'password': '123456'
            },
            status.HTTP_400_BAD_REQUEST,
            'non_field_errors'
        )
