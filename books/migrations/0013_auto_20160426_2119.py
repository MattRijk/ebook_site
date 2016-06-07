# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20160426_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
