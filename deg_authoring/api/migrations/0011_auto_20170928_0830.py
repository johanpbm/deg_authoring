# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 08:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_featuredgame_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='EduGameEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('activity_type', models.ManyToManyField(to='api.ActivityType')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edited_by', to=settings.AUTH_USER_MODEL)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edu_game_editions', to='api.DigitalEducationalGame')),
            ],
        ),
        migrations.AddField(
            model_name='activitytype',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_types', to='api.CategoryActivityType'),
        ),
        migrations.AddField(
            model_name='digitaleducationalgame',
            name='activity_type',
            field=models.ManyToManyField(to='api.ActivityType'),
        ),
    ]