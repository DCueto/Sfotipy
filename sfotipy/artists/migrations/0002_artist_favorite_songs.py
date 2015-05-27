# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='favorite_songs',
            field=models.ManyToManyField(related_name='favorite_tracks', to='tracks.Track', blank=True),
            preserve_default=True,
        ),
    ]
