# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('data', django_extensions.db.fields.json.JSONField()),
            ],
        ),
    ]
