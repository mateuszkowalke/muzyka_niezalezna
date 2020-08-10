from rest_framework import routers
from .api import (
    ArtistViewSet,
    CoverViewSet,
    GenreViewSet,
    AlbumViewSet,
    SongViewSet,
    PlaylistViewSet
)


app_name = 'song_repo'
router = routers.DefaultRouter()
router.register('api/song_repo/artists', ArtistViewSet, 'artists')
router.register('api/song_repo/covers', CoverViewSet, 'covers')
router.register('api/song_repo/genres', GenreViewSet, 'genres')
router.register('api/song_repo/albums', AlbumViewSet, 'albums')
router.register('api/song_repo/songs', SongViewSet, 'songs')
router.register('api/song_repo/playlists', PlaylistViewSet, 'playlists')

urlpatterns = router.urls
