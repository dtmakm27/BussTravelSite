# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-08 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0007_auto_20180101_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departure', models.DateTimeField(default='2000-09-04 06:00')),
                ('Arrival', models.DateTimeField(default='2000-09-04 06:00')),
                ('cityA', models.CharField(default='', max_length=250)),
                ('cityB', models.CharField(default='', max_length=250)),
                ('duration', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('fees', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='trips',
            name='changes',
        ),
    ]
