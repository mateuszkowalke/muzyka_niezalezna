from rest_framework import serializers
from song_repo.models import (
    Album,
    Song,
    Playlist
)


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'
