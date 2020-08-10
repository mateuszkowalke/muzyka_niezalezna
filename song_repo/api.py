from song_repo.models import (
    Artist,
    Cover,
    Genre,
    Album,
    Song,
    Playlist
)
from rest_framework import viewsets, permissions
from .serializers import (
    ArtistSerializer,
    CoverSerializer,
    GenreSerializer,
    AlbumSerializer,
    SongSerializer,
    PlaylistSerializer
)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArtistSerializer


class CoverViewSet(viewsets.ModelViewSet):
    queryset = Cover.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CoverSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GenreSerializer


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
