# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-09 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import lessons.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True, verbose_name='index')),
                ('title', models.CharField(max_length=75, verbose_name='title')),
                ('date', models.DateField(auto_now=True, verbose_name='date')),
                ('text', models.FileField(upload_to=lessons.models.lesson_content_path, verbose_name='content of the lesson')),
                ('is_visible', models.BooleanField(default=False, verbose_name='visible')),
            ],
        ),
    ]
