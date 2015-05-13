# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0007_attorney_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='description',
            field=models.TextField(default='DEFAULT TEXT'),
            preserve_default=False,
        ),
    ]
