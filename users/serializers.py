from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ConfirmCode

class UserBaseSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAuthSerializer(UserBaseSerializers):
    pass


class UserCreateSerializer(UserBaseSerializers):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exsists!')

class ConfirmationSerializer(serializers.Serializer):
    class Meta:
        model = ConfirmCode

