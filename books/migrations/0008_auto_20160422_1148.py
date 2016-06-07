# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20160422_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='bookhasauthor',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='bookhascategory',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
    ]
