# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20160422_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='length',
            new_name='pages',
        ),
        migrations.AddField(
            model_name='book',
            name='file_format',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='filesize',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(default=1, upload_to='pdfs/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
