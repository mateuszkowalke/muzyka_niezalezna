from ..factories import SongFactory
from song_repo.serializers import SongSerializer
from song_repo.models import Song
from rest_framework.test import APIClient
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_get_songs():
    SongFactory.create_batch(size=5)
    client = APIClient()
    response = client.get(reverse('song_repo:songs-list'))
    serializer = SongSerializer(data=Song.objects.all(), many=True)
    serializer.is_valid()
    assert response.status_code == 200
    assert len(response.data) == 5
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_post_song():
    client = APIClient()
    data = {
        'title': 'testpost',
        'duration': 2,
        'downloads': 2
    }
    response = client.post(reverse('song_repo:songs-list'), data=data)
    assert response.status_code == 201
    assert Song.objects.filter(
        title='testpost', duration=2, downloads=2).count() == 1


@pytest.mark.django_db
def test_get_valid_song():
    song = SongFactory()
    client = APIClient()
    response = client.get(reverse('song_repo:songs-detail', args=[song.id]))
    serializer = SongSerializer(song)
    print(Song.objects.get(id=song.id).file)
    assert response.status_code == 200
    # TODO
    # assert response.data == serializer.data


@ pytest.mark.django_db
def test_get_invalid_song():
    song = SongFactory()
    song.id = 't'
    client = APIClient()
    response = client.get(reverse('song_repo:songs-detail', args=[song.id]))
    assert response.status_code == 404


@ pytest.mark.django_db
def test_put_valid_song():
    song = SongFactory()
    data = {
        'title': 'new title'
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:songs-detail', args=[song.id]), data=data)
    assert response.status_code == 200
    assert Song.objects.get(id=song.id).title == 'new title'


@ pytest.mark.django_db
def test_put_invalid_song():
    song = SongFactory()
    data = {
        'title': ''
    }
    client = APIClient()
    response = client.put(
        reverse('song_repo:songs-detail', args=[song.id]), data=data)
    assert response.status_code == 400


@ pytest.mark.django_db
def test_delete_valid_song():
    song = SongFactory()
    client = APIClient()
    response = client.delete(reverse('song_repo:songs-detail', args=[song.id]))
    assert response.status_code == 204
    assert Song.objects.filter(id=song.id).count() == 0


@ pytest.mark.django_db
def test_delete_invalid_song():
    song = SongFactory()
    client = APIClient()
    response = client.delete(reverse('song_repo:songs-detail', args=['t']))
    assert response.status_code == 404
    assert Song.objects.filter(id=song.id).count() == 1
