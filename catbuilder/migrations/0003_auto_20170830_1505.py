# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catbuilder', '0002_auto_20170830_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='cat',
            name='species',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
