# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-02-06 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hire',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]
