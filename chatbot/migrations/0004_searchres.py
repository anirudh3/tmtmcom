# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_auto_20170410_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchRes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.CharField(max_length=160)),
                ('artist', models.CharField(max_length=160)),
                ('album', models.CharField(max_length=160)),
                ('uri', models.CharField(max_length=160)),
                ('created', models.DateTimeField(default=None)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
