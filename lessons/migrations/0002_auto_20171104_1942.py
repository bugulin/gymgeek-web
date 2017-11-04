# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-04 18:42
from __future__ import unicode_literals

import core.storage
import datetime
from django.db import migrations, models
import lessons.models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'permissions': (('see_hidden_lesson', 'Can see hidden lesson'),)},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='text',
            field=models.FileField(storage=core.storage.OverwriteStorage(), upload_to=lessons.models.lesson_content_path, verbose_name='content of the lesson'),
        ),
    ]