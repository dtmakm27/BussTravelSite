# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0010_remove_change_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='change',
            name='route',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='trip.Trips'),
        ),
    ]
