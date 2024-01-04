"""
Parser application configuration
"""
from django.apps import AppConfig


class ParserConfig(AppConfig):
    """Parser application configuration"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.parser'
