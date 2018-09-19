# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-19 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlHashMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('hash', models.CharField(max_length=8)),
            ],
        ),
    ]