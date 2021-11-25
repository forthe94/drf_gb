from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .views import UserModelViewSet


class TestUserViewSet(TestCase):
    def test_list_users(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)