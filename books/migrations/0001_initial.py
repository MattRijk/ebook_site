# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='BookHasAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(to='books.Author')),
                ('book', models.ForeignKey(to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='books.BookHasAuthor', to='books.Author'),
        ),
        migrations.AlterUniqueTogether(
            name='bookhasauthor',
            unique_together=set([('author', 'book')]),
        ),
    ]
