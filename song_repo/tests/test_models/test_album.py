import pytest
from rest_framework.test import APIClient
from song_repo.models import Album
from ..factories import AlbumFactory


@pytest.mark.django_db
def test_album_str():
    album = AlbumFactory()
    assert str(album) == f"Album: {album.title}"


@pytest.mark.django_db
def test_album_get_absolute_url():
    album = AlbumFactory()
    client = APIClient()
    response = client.get(album.get_absolute_url())
    assert response.status_code == 200
    assert response.data['id'] == album.id
