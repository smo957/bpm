# Generated by Django 4.0.4 on 2022-05-21 18:43

import annoying.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyUser',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('spotify_user_id', models.CharField(max_length=50)),
                ('spotify_display_name', models.CharField(max_length=191)),
                ('access_token', models.CharField(max_length=300)),
                ('refresh_token', models.CharField(max_length=300)),
                ('expiration', models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0, tzinfo=utc))),
                ('scope', models.CharField(max_length=191)),
                ('date_auth', models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='BpmPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_id', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Playlist name')),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('bpm_start', models.PositiveSmallIntegerField(help_text='Please enter a positive integer. It must be smaller or equal to the ending bpm.', verbose_name='Starting bpm')),
                ('bpm_end', models.PositiveSmallIntegerField(help_text='Please enter a positive integer. It must be greater or equal to the starting bpm.', verbose_name='Ending bpm')),
                ('multiples_bpm', models.BooleanField(default=True, help_text='If you select this, tracks with bpms that are multiples of the ones in the selected bpm range will also be added to the playlist. This means faster songs may be added, but slower songs will not be added.', verbose_name='Include multiples')),
                ('spotify_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spotify.spotifyuser')),
            ],
        ),
    ]
