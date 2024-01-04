"""
Serializers file of user application
"""
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework import validators


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for register user
    """
    username = serializers.CharField(
        required=True,
        validators=(validators.UniqueValidator(queryset=User.objects.all()),)
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=(validate_password,)
    )
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        """
        Meta class. Required to designate serializable fields.
        """
        model = User
        fields = ('username', 'password', 'confirm_password')

    def validate(self, attrs):
        """
        Validate match passwords
        """
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields did not match"}
            )
        return attrs

    def create(self, validated_data):
        """
        Create user after validating data
        """
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
