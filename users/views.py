from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from users.models import CustomUser
from users.serializers import UserSerializer, LoginSerializer


class UserView(APIView):
    def post(self, response):
        serializer = UserSerializer(data=response.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=serializer.validated_data["username"]).exists():
            return Response({"error": "username already exists"}, status=status.HTTP_409_CONFLICT)

        user = CustomUser.objects.create_user(**serializer.validated_data)

        serializer = UserSerializer(user)

        created_user = serializer.data
        created_user.pop("password")

        return Response(created_user, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(**serializer.validated_data)

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({"token": token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
