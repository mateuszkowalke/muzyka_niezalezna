import pytest
from rest_framework.test import APIClient
from song_repo.models import Cover
from ..factories import CoverFactory


@pytest.mark.django_db
def test_cover_str():
    cover = CoverFactory()
    assert str(cover) == "Cover file"
