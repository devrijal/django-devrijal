# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150920_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='updated_data',
            new_name='updated_date',
        ),
    ]
