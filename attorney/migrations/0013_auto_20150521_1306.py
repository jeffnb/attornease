# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0012_auto_20150519_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorneyuser',
            name='website',
            field=models.URLField(default=None, blank=True, null=True),
        ),
    ]
