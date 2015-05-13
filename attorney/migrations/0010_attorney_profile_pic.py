# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0009_auto_20150508_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='profile_pic',
            field=models.ImageField(default=None, null=True, blank=True, upload_to='http://attorneysprofile-dev.s3.amazonaws.com/'),
        ),
    ]
