# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0005_auto_20150504_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='year_started',
            field=models.IntegerField(default=2015),
        ),
        migrations.AlterField(
            model_name='attorney',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
