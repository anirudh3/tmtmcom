# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 05:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0018_auto_20170421_2331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ['-number']},
        ),
    ]
