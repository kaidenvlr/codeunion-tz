"""
URLs file of user application
"""
from django.urls import path

from apps.user_app import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='create-user')
]
