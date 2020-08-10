import factory
from datetime import datetime
from faker import Faker
from song_repo.models import (
    Artist,
    Cover,
    Genre,
    Album,
    Song,
    Playlist
)


fake = Faker()


class ArtistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Artist

    name = fake.first_name() + fake.last_name()


class CoverFactory(factory.DjangoModelFactory):
    class Meta:
        model = Cover

    # TODO
    # small = factory.django.FileField(
    #     data=b'small cover image', filename='fake_small_cover.jpg')
    # medium = factory.django.FileField(
    #     data=b'medium cover image', filename='fake_medium_cover.jpg')
    # large = factory.django.FileField(
    #     data=b'large cover image', filename='fake_large_cover.jpg')


class GenreFactory(factory.DjangoModelFactory):
    class Meta:
        model = Genre

    name = fake.text(max_nb_chars=128)
    default_cover = factory.SubFactory(CoverFactory)


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    title = fake.text(max_nb_chars=128)
    cover = factory.SubFactory(CoverFactory)
    release_date = fake.date()

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for genre in extracted:
                self.genres.add(genre)

    @factory.post_generation
    def artists(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for artist in extracted:
                self.artists.add(artist)


class SongFactory(factory.DjangoModelFactory):
    class Meta:
        model = Song

    title = fake.text(max_nb_chars=128)
    cover = factory.SubFactory(CoverFactory)
    # TODO
    # file = factory.django.FileField(data=b'song', filename='fake_song.mp3')
    duration = fake.random_digit()
    release_date = fake.date()
    downloads = fake.random_digit()
    buys = fake.random_digit()
    price = fake.random_int()/fake.random_int(1, 9)

    @factory.post_generation
    def artists(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for artist in extracted:
                self.artists.add(artist)

    @factory.post_generation
    def albums(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for album in extracted:
                self.albums.add(album)

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for genre in extracted:
                self.genres.add(genre)


class PlaylistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Playlist

    name = fake.text(max_nb_chars=128)
    public = fake.boolean()

    @factory.post_generation
    def songs(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for song in extracted:
                self.songs.add(song)
