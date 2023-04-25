from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAccountOwner


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
