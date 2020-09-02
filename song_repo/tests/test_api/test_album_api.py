from ..factories import AlbumFactory
from song_repo.serializers import AlbumSerializer
from song_repo.models import Album
from rest_framework.test import APIClient
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_get_albums():
    AlbumFactory.create_batch(size=5)
    client = APIClient()
    response = client.get(reverse('song_repo:albums-list'))
    serializer = AlbumSerializer(data=Album.objects.all(), many=True)
    serializer.is_valid()
    assert response.status_code == 200
    assert len(response.data) == 5
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_post_album():
    client = APIClient()
    data = {
        'title': 'test album'
    }
    response = client.post(reverse('song_repo:albums-list'), data=data)
    assert response.status_code == 201
    assert Album.objects.filter(title='test album').count() == 1


@pytest.mark.django_db
def test_get_valid_album():
    album = AlbumFactory()
    client = APIClient()
    response = client.get(reverse('song_repo:albums-detail', args=[album.id]))
    assert response.status_code == 200
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_get_invalid_album():
    album = AlbumFactory()
    album.id = 't'
    client = APIClient()
    response = client.get(reverse('song_repo:albums-detail', args=[album.id]))
    assert response.status_code == 404


@ pytest.mark.django_db
def test_put_valid_album():
    album = AlbumFactory()
    data = {
        'title': 'test album'
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:albums-detail', args=[album.id]), data=data)
    assert response.status_code == 200
    assert Album.objects.get(id=album.id).title == 'test album'


@ pytest.mark.django_db
def test_put_invalid_album():
    album = AlbumFactory()
    data = {
        'title': ''
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:albums-detail', args=[album.id]), data=data)
    assert response.status_code == 400


@ pytest.mark.django_db
def test_delete_valid_album():
    album = AlbumFactory()
    client = APIClient()
    response = client.delete(
        reverse('song_repo:albums-detail', args=[album.id]))
    assert response.status_code == 204
    assert Album.objects.filter(id=album.id).count() == 0


@ pytest.mark.django_db
def test_delete_invalid_album():
    album = AlbumFactory()
    client = APIClient()
    response = client.delete(reverse('song_repo:albums-detail', args=['t']))
    assert response.status_code == 404
    assert Album.objects.filter(id=album.id).count() == 1
