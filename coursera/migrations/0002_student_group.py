# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(default='Group #2', max_length=200),
            preserve_default=False,
        ),
    ]
