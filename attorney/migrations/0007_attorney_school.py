# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0006_auto_20150505_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='school',
            field=models.CharField(max_length=50, default='Generic Default Value'),
            preserve_default=False,
        ),
    ]
