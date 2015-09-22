# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('post', models.CharField(max_length=3000)),
                ('category_id', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=256)),
                ('is_active', models.IntegerField(default=0)),
                ('created_data', models.DateTimeField(auto_now=True)),
                ('updated_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
