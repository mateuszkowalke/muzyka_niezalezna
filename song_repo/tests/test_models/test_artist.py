import pytest
from song_repo.models import Artist
from ..factories import ArtistFactory


@pytest.mark.django_db
def test_artist_str():
    artist = ArtistFactory()
    assert str(artist) == f"Artist: {artist.name}"


@pytest.mark.django_db
def test_artist_get_absolute_url():
    pass
