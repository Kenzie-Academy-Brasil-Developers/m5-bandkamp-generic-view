from django.urls import path
from albums.views import AlbumView
from songs.views import SongView

urlpatterns = [
    path("albums/", AlbumView.as_view()),
    path("albums/<int:pk>/songs/", SongView.as_view())
]
