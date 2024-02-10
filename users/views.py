from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserAuthSerializer, ConfirmationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from random import choice
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from users import serializers




class RegistrationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')

        code = ''.join(choice('0123456789') for create in range(6))

        user = User.objects.create_user(username=username, password=password,
                                        is_active=False)
        user.code = code
        user.save()

        return Response({code},
                        status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserCreateSerializers(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#
#     code = ''.join(choice('0123456789') for created in range(6))
#
#     User.objects.create_user(username=username, password=password, is_active=False)
#     return Response(status=status.HTTP_201_CREATED)
#
#     user.code = code
#     user.save()


class AuthorizAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)  # username=admin, password=123

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def authorization_api_view(request):
#     serializer = UserAuthSerializers(data=request.data)
#     serializer.is_valid(raise_expextion=True)
#
#     user = authenticate(**serializer.validated_data)
#
#     if user:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     return Response(status=status.HTTP_401_UNAUTHORIZED)

class ConfirmAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ConfirmationSerializer

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')

        try:
            user = User.objects.get(code=code)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()

        return Response(status=status.HTTP_200_OK)


# @api_view(['POST'])
# def confirm_api_view(request):
#     serializer = ConfirmationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = request.data.get('code')
#
#     try:
#         user = User.objects.get(code=code)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     user.is_active = True
#     user.save()
#
#     return Response(status=status.HTTP_200_OK)