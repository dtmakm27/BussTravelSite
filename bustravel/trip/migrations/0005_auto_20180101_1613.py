# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-01 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_auto_20180101_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='duration_Of_Trip',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='trips',
            name='time_Of_Arrival',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='trips',
            name='time_Of_Departure',
            field=models.DateTimeField(default=''),
        ),
    ]