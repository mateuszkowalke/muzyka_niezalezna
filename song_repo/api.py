from song_repo.models import (
    Album,
    Song,
    Playlist
)
from rest_framework import viewsets, permissions
from .serializers import (
    AlbumSerializer,
    SongSerializer,
    PlaylistSerializer
)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SongSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlaylistSerializer
