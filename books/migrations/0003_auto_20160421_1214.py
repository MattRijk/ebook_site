# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160421_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('book', models.ForeignKey(to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='category',
            field=models.ForeignKey(to='books.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='bookcategory',
            unique_together=set([('book', 'category')]),
        ),
    ]
