from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from user.factories import UserFactory
from rest_framework import status

class BaseTestCase(TestCase):
    url_name = None
    url_args = None

    def _test_method_not_allowed(self, method):
        response = getattr(self.client, method)(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def setUp(self):
        self.client = APIClient()
        self.set_url()

    def set_url(self):
        self.url = reverse(self.url_name, args=self.url_args)

    def get_url(self):
        return self.url


class TestCaseAuthenticated(BaseTestCase):
    def get_user(self):
        user = getattr(self, 'user')
        if not user:
            user = UserFactory()
        return user

    def autheticate_user(self):
        self.client.force_authenticate(user=self.get_user())

    def setUp(self):
        super().setUp()
        self.autheticate_user()
