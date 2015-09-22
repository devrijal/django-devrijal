# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20150920_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='is_active',
            field=models.IntegerField(default=0, choices=[(1, b'Active'), (0, b'Inactive')]),
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(help_text=b'A short label, generally used in URLs.'),
        ),
    ]
