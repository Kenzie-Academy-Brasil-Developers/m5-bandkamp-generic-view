from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
