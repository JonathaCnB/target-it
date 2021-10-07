from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import Address, User
from users.serializers import (
    AddressFullSerializer,
    UserCreateSerializer,
    UserFullSerializer,
    UserSerializerWithToken,
)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreateViewSet(ModelViewSet):
    serializer_class = UserCreateSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        data = request.data
        password = make_password(data["password"])
        try:
            user = User.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                phone_number=data["phone_number"],
                email=data["email"],
                password=password,
            )
            user.save()
            message = {"detail": "Usuário criado com sucesso"}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception:
            message = {"detail": f"{Exception}"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    serializer_class = UserFullSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            qs = User.objects.all()
            serializer = UserFullSerializer(qs, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Usuário não possui permissão."})

    def retrieve(self, request, *args, **kwargs):
        pk = int(kwargs["pk"])
        if not request.user.is_superuser:
            if pk != request.user.id:
                return Response({"detail": "Objeto não localizado"})
        obj = User.objects.get(id=pk)
        if not obj.is_active:
            return Response({"detail": "Objeto não localizado"})
        serializer = UserFullSerializer(obj, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        pk = int(kwargs["pk"])
        if not request.user.is_superuser:
            if pk != request.user.id:
                return Response({"detail": "Objeto não localizado"})
        user = User.objects.get(id=pk)
        user.is_active = False
        user.save()
        return Response({"detail": "User deletado com sucesso!"})

    def partial_update(self, request, *args, **kwargs):
        pk = int(kwargs["pk"])
        if not request.user.is_superuser:
            if pk != request.user.id:
                return Response({"detail": "Objeto não localizado"})
        user_obj = User.objects.get(id=pk)
        if request.data["password"]:
            return Response(
                {"detail": "Para atualizar senha utilize o metodo PUT"}
            )
        serializer = UserFullSerializer(
            user_obj, data=request.data, partial=True
        )
        print(request.data["password"])
        if serializer.is_valid():
            serializer.save()
            message = {"detail": "Usuário atualizado com sucesso."}
        else:
            message = {"detail": "Usuário não atualizado."}

        return Response(message, status=status.HTTP_201_CREATED)


class AddressViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressFullSerializer

    def get_queryset(self):
        queryset = Address.objects.all()
        return queryset
