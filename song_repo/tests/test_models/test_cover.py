import pytest
from song_repo.models import Cover
from ..factories import CoverFactory


@pytest.mark.django_db
def test_cover_str():
    cover = CoverFactory()
    assert str(cover) == "Cover file"


@pytest.mark.django_db
def test_cover_get_absolute_url():
    pass
