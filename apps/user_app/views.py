"""
APIViews which will be included in `apps/user_app/urls.py` file
"""
from rest_framework import generics
from rest_framework import permissions

from apps.user_app.serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    """
    APIView to register user
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
