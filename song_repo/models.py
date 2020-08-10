from django.db import models
from django.urls import reverse


class Artist(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return f"Artist: {self.name}"


class Cover(models.Model):

    small = models.FileField(upload_to='tests')
    medium = models.FileField(upload_to='tests')
    large = models.FileField(upload_to='tests')

    def __str__(self):
        return "Cover file"


class Genre(models.Model):

    name = models.CharField(max_length=128)
    default_cover = models.ForeignKey(Cover, on_delete=models.PROTECT)

    def __str__(self):
        return f"Genre: {self.name}"


class Album(models.Model):

    title = models.CharField(max_length=128)
    artists = models.ManyToManyField(Artist)
    cover = models.ForeignKey(Cover, on_delete=models.PROTECT)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()

    def __str__(self):
        return f"Album: {self.title}"

    def get_absolute_url(self):
        return reverse('song_repo:albums-detail', kwargs={'pk': self.pk})


class Song(models.Model):

    title = models.CharField(max_length=128)
    artists = models.ManyToManyField(Artist, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    cover = models.ForeignKey(
        Cover, on_delete=models.PROTECT, null=True, blank=True)
    file = models.FileField(upload_to='songs', null=True, blank=True)
    duration = models.PositiveSmallIntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    downloads = models.IntegerField(default=0)
    buys = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Song: {self.title}"

    def get_absolute_url(self):
        return reverse('song_repo:songs-detail', kwargs={'pk': self.pk})

    def get_song_cover(self):
        if self.cover:
            return self.cover.small
        if self.albums.all():
            return self.albums.all()[0].cover.small
        if self.genres.all():
            return self.genres.all()[0].default_cover.small

    def get_song_release_date(self):
        if self.release_date:
            return self.release_date
        if self.albums.all():
            return self.albums.all()[0].release_date


class Playlist(models.Model):

    name = models.CharField(max_length=128)
    songs = models.ManyToManyField(Song)
    # TODO - add to factory
    owner = None
    public = models.BooleanField()

    def __str__(self):
        return f"Playlist: {self.name}"

    def get_absolute_url(self):
        return reverse('song_repo:playlists-detail', kwargs={'pk': self.pk})
