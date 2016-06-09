# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20160427_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='pdfs/%Y/%m/%d'),
        ),
    ]
