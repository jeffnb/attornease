# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import localflavor.us.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150519_1550'),
        ('attorney', '0011_auto_20150513_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttorneyUser',
            fields=[
                ('baseattorneaseuser_ptr', models.OneToOneField(auto_created=True, to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False, parent_link=True)),
                ('firm', models.CharField(max_length=100)),
                ('phone', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('website', models.URLField(blank=True, default=None)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=7)),
                ('school', models.CharField(max_length=50)),
                ('year_started', models.IntegerField(default=2015)),
                ('description', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, upload_to='', null=True, default=None)),
                ('categories', models.ManyToManyField(to='attorney.LawCategory')),
                ('service_areas', models.ManyToManyField(to='attorney.ServiceArea')),
            ],
            options={
                'verbose_name': 'Attorney User',
            },
            bases=('accounts.baseattorneaseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='firmaddress',
            name='attorney',
            field=models.ForeignKey(to='attorney.AttorneyUser'),
        ),
        migrations.AlterField(
            model_name='license',
            name='attorney',
            field=models.ForeignKey(to='attorney.AttorneyUser'),
        ),
    ]
