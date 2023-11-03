from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.parser.models import Currency


class CurrencyTests(APITestCase):
    def mock_get_token(self, create=True):
        if create:
            User.objects.create_superuser(username=settings.SUPERUSER_USERNAME, password=settings.SUPERUSER_PASSWORD)
        url = reverse('api-token-auth')
        data = {'username': settings.SUPERUSER_USERNAME, 'password': settings.SUPERUSER_PASSWORD}
        response = self.client.post(url, data=data)
        return response

    def test_get_token(self):
        response = self.mock_get_token()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_token_error(self):
        response = self.mock_get_token(create=False)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_get_currencies(self):
        token = self.mock_get_token().data['token']
        url = reverse(viewname='currencies')
        response = self.client.get(url, format='json', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_currency(self):
        token = self.mock_get_token().data['token']
        Currency.objects.create(name="SUP", rate=123.12)
        url = reverse(viewname='currency', kwargs={'pk': 1})
        response = self.client.get(url, format='json', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"id": 1, "name": "SUP", "rate": 123.12})

    def test_get_currency_error(self):
        token = self.mock_get_token().data['token']
        url = reverse(viewname='currency', kwargs={'pk': 1})
        response = self.client.get(url, format='json', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
