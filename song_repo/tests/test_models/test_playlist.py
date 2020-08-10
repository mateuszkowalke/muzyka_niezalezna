import pytest
from rest_framework.test import APIClient
from song_repo.models import Playlist
from ..factories import PlaylistFactory


@pytest.mark.django_db
def test_playlist_str():
    playlist = PlaylistFactory()
    assert str(playlist) == f"Playlist: {playlist.name}"


@pytest.mark.django_db
def test_playlist_get_absolute_url():
    playlist = PlaylistFactory()
    client = APIClient()
    response = client.get(playlist.get_absolute_url())
    assert response.status_code == 200
    assert response.data['id'] == playlist.id
