# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20160422_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookhasauthor',
            name='title',
        ),
        migrations.RemoveField(
            model_name='bookhascategory',
            name='title',
        ),
        migrations.AlterField(
            model_name='bookhasauthor',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='bookhascategory',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
