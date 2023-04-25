from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from songs.models import Song
from songs.serializers import SongSerializer

from albums.models import Album


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album=self.kwargs.get("pk"))

    def perform_create(self, serializer):
        album = Album.objects.get(id=self.kwargs.get("pk"))
        serializer.save(album=album)
