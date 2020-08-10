import pytest
from rest_framework.test import APIClient
from song_repo.models import Artist
from ..factories import ArtistFactory


@pytest.mark.django_db
def test_artist_str():
    artist = ArtistFactory()
    assert str(artist) == f"Artist: {artist.name}"
