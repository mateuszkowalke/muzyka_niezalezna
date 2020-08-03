from song_repo.models import Song
from rest_framework import viewsets, permissions
from .serializers import SongSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SongSerializer
