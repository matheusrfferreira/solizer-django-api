from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    cell_phone_number = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255, required=True)
    cpf = serializers.CharField(max_length=11, required=True)
    cnpj = serializers.CharField(max_length=14, required=False)
    user_type = serializers.IntegerField(required=True)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)


class ClientSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    cell_phone_number = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)


class IntegratorSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    cell_phone_number = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
