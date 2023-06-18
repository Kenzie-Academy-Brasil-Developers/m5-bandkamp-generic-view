from django.urls import path

from .views import *

urlpatterns = [
    path("songs/", SongView.as_view()),
]