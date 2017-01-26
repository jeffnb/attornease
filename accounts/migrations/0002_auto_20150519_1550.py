# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attorneyuser',
            name='baseattorneaseuser_ptr',
        ),
        migrations.RemoveField(
            model_name='attorneyuser',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='attorneyuser',
            name='service_areas',
        ),
        migrations.DeleteModel(
            name='AttorneyUser',
        ),
    ]
