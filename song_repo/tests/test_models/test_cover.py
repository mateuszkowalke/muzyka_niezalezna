import pytest
from rest_framework.test import APIClient
from song_repo.models import Cover
from ..factories import CoverFactory


@pytest.mark.django_db
def test_cover_str():
    cover = CoverFactory()
    assert str(cover) == "Cover file"


@pytest.mark.django_db
def test_cover_get_absolute_url():
    cover = CoverFactory()
    client = APIClient()
    response = client.get(cover.get_absolute_url())
    assert response.status_code == 200
    assert response.data['id'] == cover.id
