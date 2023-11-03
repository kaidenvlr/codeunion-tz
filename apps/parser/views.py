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

    @action(detail=True, methods=('get',))
    def retrieve(self, request, id: int, *args, **kwargs):
        try:
            queryset = Currency.objects.get(id=id)
            serializer = self.serializer_class(queryset)
            return Response({"status": "ok", "data": serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"status": "error", "description": "Currency does not exist."},
                            status=status.HTTP_404_NOT_FOUND)
