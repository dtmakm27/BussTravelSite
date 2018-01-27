# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-01 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_Of_Departure', models.DateTimeField(default='2012-09-04 06:00')),
                ('time_Of_Arrival', models.DateTimeField(default='2012-09-04 06:00')),
                ('city_Of_Departure', models.CharField(default='', max_length=250)),
                ('city_Of_Arrival', models.CharField(default='', max_length=250)),
                ('changes', models.CharField(default='', max_length=250)),
                ('duration_Of_Trip', models.TimeField(default=0)),
                ('fees', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
    ]
