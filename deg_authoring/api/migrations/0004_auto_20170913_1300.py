# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_intendedlearningoutcome_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dgblinstructionaldesign',
            old_name='ilo',
            new_name='ilos',
        ),
    ]
