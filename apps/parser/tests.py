"""Tests for parser application"""
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.parser.models import Currency


class CurrencyTests(APITestCase):
    """Currency model tests"""
    def mock_get_token(self, create=True):
        """Mock for getting token"""
        if create:
            User.objects.create_superuser(
                username=settings.SUPERUSER_USERNAME,
                password=settings.SUPERUSER_PASSWORD
            )
        url = reverse('api-token-auth')
        data = {'username': settings.SUPERUSER_USERNAME, 'password': settings.SUPERUSER_PASSWORD}
        response = self.client.post(url, data=data)
        return response

    def test_get_token(self):
        """Test of getting token with mock function"""
        response = self.mock_get_token()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_token_error(self):
        """Test of getting error while getting token with mock function"""
        response = self.mock_get_token(create=False)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_currencies(self):
        """Test get list of currencies"""
        token = self.mock_get_token().data['access']
        url = reverse(viewname='currencies')
        response = self.client.get(url, format='json', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_currency(self):
        """Test of get exact currency's rate"""
        token = self.mock_get_token().data['access']
        Currency.objects.create(name="SUP", rate=123.12)
        url = reverse(viewname='currency', kwargs={'pk': 1})
        response = self.client.get(url, format='json', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"id": 1, "name": "SUP", "rate": 123.12})

    def test_get_currency_error(self):
        """Test of get unknown currency's rate"""
        token = self.mock_get_token().data['access']
        url = reverse(viewname='currency', kwargs={'pk': 1})
        response = self.client.get(url, format='json', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
