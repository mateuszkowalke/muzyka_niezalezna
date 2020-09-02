from rest_framework import routers
from .api import (
    AlbumViewSet,
    SongViewSet,
    PlaylistViewSet
)


app_name = 'song_repo'
router = routers.DefaultRouter()
router.register('api/song_repo/albums', AlbumViewSet, 'albums')
router.register('api/song_repo/playlists', PlaylistViewSet, 'playlists')
router.register('api/song_repo', SongViewSet, 'songs')


urlpatterns = router.urls
