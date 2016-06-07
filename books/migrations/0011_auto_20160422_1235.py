# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20160422_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookhasauthor',
            name='name',
            field=models.CharField(max_length=45, blank=True),
        ),
        migrations.AddField(
            model_name='bookhascategory',
            name='title',
            field=models.CharField(max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='bookhasauthor',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bookhascategory',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID'),
        ),
    ]
