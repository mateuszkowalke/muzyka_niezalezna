# Generated by Django 3.0.8 on 2020-07-16 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song_repo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small', models.FileField(upload_to='')),
                ('medium', models.FileField(upload_to='')),
                ('large', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Cover',
                'verbose_name_plural': 'Covers',
            },
        ),
        migrations.AddField(
            model_name='song',
            name='buys',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('public', models.BooleanField()),
                ('songs', models.ManyToManyField(to='song_repo.Song')),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('default_cover', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='song_repo.Cover')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
                ('artist', models.ManyToManyField(to='song_repo.Artist')),
                ('cover', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='song_repo.Cover')),
                ('genre', models.ManyToManyField(to='song_repo.Genre')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(to='song_repo.Album'),
        ),
        migrations.AddField(
            model_name='song',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='song_repo.Cover'),
        ),
        migrations.AddField(
            model_name='song',
            name='genres',
            field=models.ManyToManyField(to='song_repo.Genre'),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='song_repo.Artist'),
        ),
    ]
