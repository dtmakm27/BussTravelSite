# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-01 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_auto_20180101_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='duration_Of_Trip',
            field=models.TimeField(default='06:00'),
        ),
    ]
