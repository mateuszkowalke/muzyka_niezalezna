import pytest
from song_repo.models import Genre
from ..factories import GenreFactory


@pytest.mark.django_db
def test_genre_str():
    genre = GenreFactory()
    assert str(genre) == f"Genre: {genre.name}"


@pytest.mark.django_db
def test_genre_get_absolute_url():
    pass
