"""
Admin models configuration for parser application
"""
from django.contrib import admin

from apps.parser.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """
    Currency Admin Model
    """
    list_display = ('id', 'name', 'rate')
