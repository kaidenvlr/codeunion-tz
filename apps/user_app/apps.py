"""
User application define
"""
from django.apps import AppConfig


class UserAppConfig(AppConfig):
    """
    User application configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user_app'
