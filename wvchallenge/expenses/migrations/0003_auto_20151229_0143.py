# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20151229_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='desc',
            field=models.CharField(max_length=255, unique_for_date=models.DateField()),
        ),
    ]