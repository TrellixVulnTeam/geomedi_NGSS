# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-21 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karte', '0009_auto_20180121_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='reference',
            field=models.TextField(default=''),
        ),
    ]