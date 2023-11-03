from rest_framework import generics

from apps.parser.classes import Pagination
from apps.parser.models import Currency
from apps.parser.serializers import CurrencySerializer


class AllCurrencyAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = Pagination


class CurrencyAPIView(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    lookup_field = 'pk'
