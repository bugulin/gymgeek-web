# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170912_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'group', 'verbose_name_plural': 'groups'},
        ),
        migrations.RemoveField(
            model_name='group',
            name='code',
        ),
        migrations.AddField(
            model_name='group',
            name='auth_key',
            field=models.CharField(max_length=32, unique=True, verbose_name='secret code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
