import pytest
from song_repo.models import Playlist
from ..factories import PlaylistFactory


@pytest.mark.django_db
def test_playlist_str():
    playlist = PlaylistFactory()
    assert str(playlist) == f"Playlist: {playlist.name}"


@pytest.mark.django_db
def test_playlist_get_absolute_url():
    pass
