# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20160609_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='pdfs/'),
        ),
    ]
