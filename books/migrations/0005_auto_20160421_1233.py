# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160421_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookhascategory',
            options={'verbose_name_plural': 'Book has categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='books',
            field=models.ManyToManyField(to='books.Book', through='books.BookHasCategory'),
        ),
    ]
