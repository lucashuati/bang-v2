from django.test import TestCase
from user.factories import UserFactory


class FactoryTestCase(TestCase):

    def test_create_factories(self):
        UserFactory()

    def test_create_batch_factories(self):
        UserFactory.create_batch(5)
