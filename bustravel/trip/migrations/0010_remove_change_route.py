# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0009_auto_20180108_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='change',
            name='route',
        ),
    ]
