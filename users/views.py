from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from users.serializers import UserSerializer, LoginSerializer, ClientSerializer, IntegratorSerializer


class UserView(APIView):
    def post(self, response):
        serializer = UserSerializer(data=response.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=serializer.validated_data["username"]).exists():
            return Response({"error": "username already exists"}, status=status.HTTP_409_CONFLICT)

        if not serializer.data.get("user_type") in [1, 2]:
            return Response({"error": "user_type must be 1 or 2"}, status=status.HTTP_400_BAD_REQUEST)
        
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

class EditUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializered_user = UserSerializer(user)
        return Response(serializered_user.data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        serializered_user_data = UserSerializer(data=request.data)
        
        if not serializered_user_data.is_valid():
            return Response(serializered_user_data.errors, status=status.HTTP_400_BAD_REQUEST)

        if user_id != request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = get_object_or_404(CustomUser, id=user_id)
        except:
            return Response({"errors": "invalid user_id"}, status=status.HTTP_404_NOT_FOUND)

        user2 = UserSerializer(user)
       
        user_username = serializered_user_data.data.get('username')
        
        if user_username:
            if user_username == user2.data.get('username'):
                del serializered_user_data.data['username']
            else:
                if CustomUser.objects.filter(username=user_username).exists():
                    return Response({"error": "username already exists"}, status=status.HTTP_409_CONFLICT) 
        

        updated_user = CustomUser.objects.filter(id=user_id).update(**serializered_user_data.validated_data)
        
        serializered_updated_user = UserSerializer(updated_user)
        
        return Response(serializered_updated_user.data, status=status.HTTP_200_OK)


class ClientView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        client = 1
        clients = CustomUser.objects.filter(user_type=client)
        if not clients:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializered_clients = ClientSerializer(clients, many=True)
        return Response(serializered_clients.data, status=status.HTTP_200_OK)


class IntegratorView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        integrator = 2
        integrators = CustomUser.objects.filter(user_type=integrator)
        if not integrators:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializered_integrators = IntegratorSerializer(integrators, many=True)
        return Response(serializered_integrators.data, status=status.HTTP_200_OK)
