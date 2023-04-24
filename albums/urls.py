from django.urls import path
from albums.views import AlbumView

urlpatterns = [
    path("albums/", AlbumView.as_view())
]
