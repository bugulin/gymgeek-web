# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-05 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171004_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=2000, verbose_name='text'),
        ),
    ]
