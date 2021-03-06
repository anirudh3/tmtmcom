# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0023_auto_20170422_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatters',
            name='acousticness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='danceability',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='energy',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='instrumentalness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='key',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='liveness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='loudness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='speechiness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='tempo',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='time_signature',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='chatters',
            name='valence',
            field=models.FloatField(default=0, null=True),
        ),
    ]
