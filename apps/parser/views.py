from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.parser.classes import Pagination
from apps.parser.models import Currency
from apps.parser.serializers import CurrencySerializer


# Можно сделать Views с помощью rest_framework.generics, можно через декораторы.
class AllCurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = Pagination
    permission_classes = (permissions.AllowAny,)


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CurrencySerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return Currency.objects.all()

    @action(detail=True, methods=('get',))
    def retrieve(self, request, pk: int, *args, **kwargs):
        queryset = self.get_queryset()
        currency = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(currency)
        return Response(serializer.data)
