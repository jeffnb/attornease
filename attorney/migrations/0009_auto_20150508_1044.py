# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0008_attorney_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmaddress',
            name='postal',
            field=localflavor.us.models.USZipCodeField(db_index=True, max_length=10),
        ),
    ]
