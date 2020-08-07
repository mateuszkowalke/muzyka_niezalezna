import pytest
from song_repo.models import Album
from ..factories import AlbumFactory


@pytest.mark.django_db
def test_album_str():
    album = AlbumFactory()
    assert str(album) == f"Album: {album.title}"


@pytest.mark.django_db
def test_album_get_absolute_url():
    pass
