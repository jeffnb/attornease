# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

categories = [
    'Bankruptcy (personal)',
    'Bankruptcy (business)',
    'Bankruptcy (creditors)',
    'Business/Commercial law',
    'Business Formation',
    'Constitutional law',
    'Construction law',
    'Consumer law',
    'Contracts law (drafting, reviewing, disputes)',
    'Corporate Counsel',
    'Criminal law - Traffic violations',
    'Criminal law - DUI',
    'Criminal law - Other',
    'Internet/Cyber law',
    'Elder law',
    'Employment/labor law',
    'Entertainment law',
    'Family law',
    'Gaming law',
    'Immigration law',
    'Insurance law',
    'Intellectual property law (Trademark, Copyright)',
    'Intellectual property law (Patents)',
    'Landlord/Tenant Law (landlord focus)',
    'Landlord/Tenant Law (tenant focus)',
    'Land use & zoning law',
    'Medical Malpractice',
    'Other (or not sure): Civil',
    'Personal Injury/Tort Law (traffic accident, slip and fall, etc.)',
    'Probate, Wills, Trusts & Estates',
    'Product liability',
    'Real estate/Property law',
    'Securities and Finance',
    'Tax law',
]


def load_categories(apps, schema_editor):
    """
    This will loop through categories and try to add them to the database
    :param apps:
    :param schema_editor:
    :return: nothing
    """
    LawCategory = apps.get_model('attorney', "LawCategory")

    for cateogry in categories:
        LawCategory(title=cateogry).save()

class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_categories)
    ]
