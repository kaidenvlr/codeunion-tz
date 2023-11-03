from rest_framework import generics
from rest_framework import permissions

from apps.user_app.serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
