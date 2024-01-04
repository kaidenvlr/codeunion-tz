"""
Views file for parser application
"""
from rest_framework import generics

from apps.parser.classes import Pagination
from apps.parser.models import Currency
from apps.parser.serializers import CurrencySerializer


class AllCurrencyAPIView(generics.ListAPIView):
    """
    APIView for getting list of all currencies
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = Pagination


class CurrencyAPIView(generics.RetrieveAPIView):
    """
    APIView for getting current currency of exact exchange
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    lookup_field = 'pk'
