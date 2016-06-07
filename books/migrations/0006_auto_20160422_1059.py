# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20160421_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='length',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
