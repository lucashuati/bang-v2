from base.tests import TestCaseAuthenticated
from user.serializers import UserSerializer
from user.factories import UserFactory
from rest_framework import status

class ListUsersTestCase(TestCaseAuthenticated):

    @classmethod
    def setUpTestData(cls):
        cls.users = UserFactory.create_batch(5)
        cls.user = cls.users[0]
        cls.url_name = 'user-list'

    def test_list_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserSerializer(self.users, many=True).data)

class UpdateUserTestCase(TestCaseAuthenticated):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url_name = 'user-detail'
        cls.url_args = [cls.user.pk]

    def test_update_user(self):
        data = { 'last_name': 'Updated name' }
        response = self.client.patch(self.url, data)
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserSerializer(self.user).data)
        self.assertEqual(data['last_name'], self.user.last_name)
