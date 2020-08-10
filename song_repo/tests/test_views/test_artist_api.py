from ..factories import ArtistFactory
from song_repo.serializers import ArtistSerializer
from song_repo.models import Artist
from rest_framework.test import APIClient
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_get_artists():
    ArtistFactory.create_batch(size=5)
    client = APIClient()
    response = client.get(reverse('song_repo:artists-list'))
    serializer = ArtistSerializer(data=Artist.objects.all(), many=True)
    serializer.is_valid()
    assert response.status_code == 200
    assert len(response.data) == 5
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_post_artist():
    client = APIClient()
    data = {
        'name': 'new artist'
    }
    response = client.post(reverse('song_repo:artists-list'), data=data)
    assert response.status_code == 201
    assert Artist.objects.filter(name='new artist').count() == 1


@pytest.mark.django_db
def test_get_valid_artist():
    artist = ArtistFactory()
    client = APIClient()
    response = client.get(
        reverse('song_repo:artists-detail', args=[artist.id]))
    assert response.status_code == 200
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_get_invalid_artist():
    artist = ArtistFactory()
    artist.id = 't'
    client = APIClient()
    response = client.get(
        reverse('song_repo:artists-detail', args=[artist.id]))
    assert response.status_code == 404


@ pytest.mark.django_db
def test_put_valid_artist():
    artist = ArtistFactory()
    data = {
        'name': 'new artist'
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:artists-detail', args=[artist.id]), data=data)
    assert response.status_code == 200
    assert Artist.objects.get(id=artist.id).name == 'new artist'


@ pytest.mark.django_db
def test_put_invalid_artist():
    artist = ArtistFactory()
    data = {
        'title': ''
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:artists-detail', args=[artist.id]), data=data)
    assert response.status_code == 400


@ pytest.mark.django_db
def test_delete_valid_artist():
    artist = ArtistFactory()
    client = APIClient()
    response = client.delete(
        reverse('song_repo:artists-detail', args=[artist.id]))
    assert response.status_code == 204
    assert Artist.objects.filter(id=artist.id).count() == 0


@ pytest.mark.django_db
def test_delete_invalid_artist():
    artist = ArtistFactory()
    client = APIClient()
    response = client.delete(reverse('song_repo:artists-detail', args=['t']))
    assert response.status_code == 404
    assert Artist.objects.filter(id=artist.id).count() == 1
