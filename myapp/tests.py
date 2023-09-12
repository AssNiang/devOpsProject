from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Visit

# Create your tests here.


class UserListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-list')
        self.user_data = {'username': 'testuser', 'email': 'test@example.com', 'first_name': 'Test',
                          'last_name': 'User'}
        self.user = User.objects.create(**self.user_data)

    def test_get_user_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['username'], self.user.username)


class VisitCountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('visit-count')
        self.visit = Visit.objects.create(count=0)

    def test_get_visit_count(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

