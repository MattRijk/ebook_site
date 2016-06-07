# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160421_1214'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookcategory',
            new_name='BookHasCategory',
        ),
    ]
