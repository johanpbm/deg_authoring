# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dgblinstructionaldesign',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
