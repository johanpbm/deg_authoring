# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170921_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('digital_educational_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DigitalEducationalGame')),
            ],
        ),
    ]