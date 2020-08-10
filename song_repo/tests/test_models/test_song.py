import pytest
from rest_framework.test import APIClient
from song_repo.models import Song
from ..factories import (
    SongFactory,
    AlbumFactory,
    GenreFactory,
    CoverFactory
)


@pytest.mark.django_db
def test_song_get_song_cover():
    song1 = SongFactory(cover=CoverFactory())
    assert song1.get_song_cover() == song1.cover.small
    song2 = SongFactory(cover=None, albums=[
                        AlbumFactory(cover=CoverFactory())])
    assert song2.get_song_cover() == song2.albums.all()[0].cover.small
    song3 = SongFactory(cover=None, genres=[
                        GenreFactory(default_cover=CoverFactory())])
    assert song3.get_song_cover() == song3.genres.all()[0].default_cover.small


@pytest.mark.django_db
def test_song_get_song_release_date():
    song = SongFactory()
    db_song_date = Song.objects.get(id=song.id).get_song_release_date()
    assert db_song_date.strftime('%Y-%m-%d') == song.release_date
    song2 = SongFactory(release_date=None, albums=[AlbumFactory()])
    db_song2 = Song.objects.get(id=song2.id)
    assert db_song2.get_song_release_date() == song2.albums.all()[
        0].release_date


@pytest.mark.django_db
def test_song_str():
    song = SongFactory()
    assert str(song) == f"Song: {song.title}"


@pytest.mark.django_db
def test_song_get_absolute_url():
    song = SongFactory()
    client = APIClient()
    response = client.get(song.get_absolute_url())
    assert response.status_code == 200
    assert response.data['id'] == song.id
