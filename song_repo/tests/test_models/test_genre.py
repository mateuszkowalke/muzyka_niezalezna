import pytest
from rest_framework.test import APIClient
from song_repo.models import Genre
from ..factories import GenreFactory


@pytest.mark.django_db
def test_genre_str():
    genre = GenreFactory()
    assert str(genre) == f"Genre: {genre.name}"


@pytest.mark.django_db
def test_genre_get_absolute_url():
    genre = GenreFactory()
    client = APIClient()
    response = client.get(genre.get_absolute_url())
    assert response.status_code == 200
    assert response.data['id'] == genre.id
