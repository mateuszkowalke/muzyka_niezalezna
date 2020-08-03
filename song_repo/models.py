from django.db import models
from django.urls import reverse


class Artist(models.Model):

    name = models.CharField(max_length=128)

    class Meta:

        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return f"Artist: {self.name}"

    def get_absolute_url(self):
        # TODO
        return reverse('', kwargs={'pk': self.pk})


class Cover(models.Model):

    small = models.FileField(upload_to='tests')
    medium = models.FileField(upload_to='tests')
    large = models.FileField(upload_to='tests')

    class Meta:

        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'

    def __str__(self):
        return "Cover file"

    def get_absolute_url(self):
        # TODO
        return reverse('', kwargs={'pk': self.pk})


class Genre(models.Model):

    name = models.CharField(max_length=128)
    default_cover = models.ForeignKey(Cover, on_delete=models.PROTECT)

    class Meta:

        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return f"Genre: {self.title}"

    def get_absolute_url(self):
        # TODO
        return reverse('', kwargs={'pk': self.pk})


class Album(models.Model):

    title = models.CharField(max_length=128)
    artists = models.ManyToManyField(Artist)
    cover = models.ForeignKey(Cover, on_delete=models.PROTECT)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()

    class Meta:

        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return f"Album: {self.title}"

    def get_absolute_url(self):
        # TODO
        return reverse('', kwargs={'pk': self.pk})


class Song(models.Model):

    title = models.CharField(max_length=128, null=True, blank=True)
    artists = models.ManyToManyField(Artist)
    albums = models.ManyToManyField(Album)
    genres = models.ManyToManyField(Genre)
    cover = models.ForeignKey(
        Cover, on_delete=models.PROTECT, null=True, blank=True)
    file = models.FileField(upload_to='tests', null=True, blank=True)
    duration = models.PositiveSmallIntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    downloads = models.IntegerField(default=0)
    buys = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:

        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return f"Song: {self.title}"

    def get_absolute_url(self):
        # TODO
        return reverse('', kwargs={'pk': self.pk})

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
    # TODO
    owner = None
    public = models.BooleanField()

    class Meta:

        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return f"Playlist: {self.name}"

    def get_absolute_url(self):
        # TODO
        return reverse('', kwargs={'pk': self.pk})
