# Generated by Django 3.1 on 2020-08-10 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song_repo', '0006_auto_20200807_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, to='song_repo.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='song_repo.cover'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(blank=True, to='song_repo.Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
