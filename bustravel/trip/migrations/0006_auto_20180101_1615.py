# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-01 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_auto_20180101_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='time_Of_Arrival',
            field=models.DateTimeField(default='0-0-0 00:00'),
        ),
        migrations.AlterField(
            model_name='trips',
            name='time_Of_Departure',
            field=models.DateTimeField(default='0-0-0 00:00'),
        ),
    ]
