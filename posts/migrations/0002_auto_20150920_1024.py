# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post',
            new_name='content',
        ),
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
