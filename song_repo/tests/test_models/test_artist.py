import pytest
from rest_framework.test import APIClient
from song_repo.models import Artist
from ..factories import ArtistFactory


@pytest.mark.django_db
def test_artist_str():
    artist = ArtistFactory()
    assert str(artist) == f"Artist: {artist.name}"


@pytest.mark.django_db
def test_artist_get_absolute_url():
    artist = ArtistFactory()
    client = APIClient()
    response = client.get(artist.get_absolute_url())
    assert response.status_code == 200
    assert response.data['id'] == artist.id
