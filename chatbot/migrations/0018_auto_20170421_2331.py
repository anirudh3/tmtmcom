# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0017_auto_20170421_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
