
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from users.models import User
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        album_id = self.kwargs.get("pk")
        serializer.save(album_id=album_id)

    def get_queryset(self):
        self.pagination_class.page_size = 1
        return self.paginate_queryset(self.queryset)
