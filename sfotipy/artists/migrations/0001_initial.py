# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255, blank=True)),
                ('biography', models.TextField(blank=True)),
                ('favorite_songs', models.ManyToManyField(related_name='is_favorite_of', to='tracks.Track', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
