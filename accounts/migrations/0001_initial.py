# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0011_auto_20150513_1028'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAttornEaseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30)),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AttorneyUser',
            fields=[
                ('baseattorneaseuser_ptr', models.OneToOneField(parent_link=True, serialize=False, to=settings.AUTH_USER_MODEL, auto_created=True, primary_key=True)),
                ('firm', models.CharField(max_length=100)),
                ('phone', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('website', models.URLField(blank=True, default=None)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=7)),
                ('school', models.CharField(max_length=50)),
                ('year_started', models.IntegerField(default=2015)),
                ('description', models.TextField()),
                ('profile_pic', models.ImageField(null=True, upload_to='', default=None, blank=True)),
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
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('baseattorneaseuser_ptr', models.OneToOneField(parent_link=True, serialize=False, to=settings.AUTH_USER_MODEL, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Staff User',
            },
            bases=('accounts.baseattorneaseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='baseattorneaseuser',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', blank=True, related_query_name='user', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set'),
        ),
        migrations.AddField(
            model_name='baseattorneaseuser',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', blank=True, related_query_name='user', to='auth.Permission', help_text='Specific permissions for this user.', related_name='user_set'),
        ),
    ]
