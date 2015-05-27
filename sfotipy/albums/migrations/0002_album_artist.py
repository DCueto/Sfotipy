# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='artists.Artist'),
            preserve_default=True,
        ),
    ]
