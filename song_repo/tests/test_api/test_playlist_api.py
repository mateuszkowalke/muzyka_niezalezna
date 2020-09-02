from ..factories import PlaylistFactory
from song_repo.serializers import PlaylistSerializer
from song_repo.models import Playlist
from rest_framework.test import APIClient
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_get_playlists():
    PlaylistFactory.create_batch(size=5)
    client = APIClient()
    response = client.get(reverse('song_repo:playlists-list'))
    serializer = PlaylistSerializer(data=Playlist.objects.all(), many=True)
    serializer.is_valid()
    assert response.status_code == 200
    assert len(response.data) == 5
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_post_playlist():
    client = APIClient()
    data = {
        'name': 'test playlist'
    }
    response = client.post(reverse('song_repo:playlists-list'), data=data)
    assert response.status_code == 201
    assert Playlist.objects.filter(name='test playlist').count() == 1


@pytest.mark.django_db
def test_get_valid_playlist():
    playlist = PlaylistFactory()
    client = APIClient()
    response = client.get(
        reverse('song_repo:playlists-detail', args=[playlist.id]))
    assert response.status_code == 200
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_get_invalid_playlist():
    playlist = PlaylistFactory()
    playlist.id = 't'
    client = APIClient()
    response = client.get(
        reverse('song_repo:playlists-detail', args=[playlist.id]))
    assert response.status_code == 404


@ pytest.mark.django_db
def test_put_valid_playlist():
    playlist = PlaylistFactory()
    data = {
        'name': 'test playlist'
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:playlists-detail', args=[playlist.id]), data=data)
    assert response.status_code == 200
    assert Playlist.objects.get(id=playlist.id).name == 'test playlist'


@ pytest.mark.django_db
def test_put_invalid_playlist():
    playlist = PlaylistFactory()
    data = {
        'name': ''
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:playlists-detail', args=[playlist.id]), data=data)
    assert response.status_code == 400


@ pytest.mark.django_db
def test_delete_valid_playlist():
    playlist = PlaylistFactory()
    client = APIClient()
    response = client.delete(
        reverse('song_repo:playlists-detail', args=[playlist.id]))
    assert response.status_code == 204
    assert Playlist.objects.filter(id=playlist.id).count() == 0


@ pytest.mark.django_db
def test_delete_invalid_playlist():
    playlist = PlaylistFactory()
    client = APIClient()
    response = client.delete(reverse('song_repo:playlists-detail', args=['t']))
    assert response.status_code == 404
    assert Playlist.objects.filter(id=playlist.id).count() == 1
