# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20160422_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-published',)},
        ),
    ]
