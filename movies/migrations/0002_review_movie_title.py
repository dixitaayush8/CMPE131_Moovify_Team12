# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie_title',
            field=models.CharField(default='', max_length=100),
        ),
    ]