# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20150920_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(max_length=3000),
        ),
    ]
