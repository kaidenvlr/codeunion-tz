from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('create-user')
        data = {
            'username': 'user',
            'password': 'Password123@',
            'confirm_password': 'Password123@'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_weak_password(self):
        url = reverse('create-user')
        data = {
            'username': 'user',
            'password': 'weakpas',
            'confirm_password': 'weakpas'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_error_match_passwords(self):
        url = reverse('create-user')
        data = {
            'username': 'user',
            'password': 'password',
            'confirm_password': 'username'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_error_unique_username(self):
        url = reverse('create-user')
        data = {
            'username': 'user',
            'password': 'Password123@',
            'confirm_password': 'Password123@'
        }
        self.client.post(url, data=data)
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
