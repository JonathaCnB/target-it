from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import Address, User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "cpf",
        ]


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializerWithToken(UserFullSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_superuser", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class AddressFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
