"""Serializers file of parser application"""
from rest_framework import serializers

from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """Currency Serializer"""
    class Meta:
        """Meta class. Need to define serializable fields."""
        model = Currency
        fields = ('id', 'name', 'rate')
