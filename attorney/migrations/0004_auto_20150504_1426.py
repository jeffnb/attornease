# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0003_auto_20150504_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawcategory',
            name='attorneys',
        ),
        migrations.AddField(
            model_name='attorney',
            name='categories',
            field=models.ManyToManyField(to='attorney.LawCategory'),
            preserve_default=True,
        ),
    ]
